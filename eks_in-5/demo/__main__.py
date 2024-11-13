import pulumi
import pulumi_awsx as awsx
import pulumi_eks as eks
import pulumi_kubernetes as k8s
import json

# Create VPC with default CIDR
eks_vpc = awsx.ec2.Vpc("eks-vpc",
    enable_dns_hostnames=True)

# Create minimal EKS cluster
eks_cluster = eks.Cluster("eks-cluster",
    vpc_id=eks_vpc.vpc_id,
    private_subnet_ids=eks_vpc.private_subnet_ids,
    public_subnet_ids=eks_vpc.public_subnet_ids,
    fargate=True,  
)

# Create Kubernetes provider using the EKS cluster
k8s_provider = k8s.Provider('k8s-provider',
    kubeconfig=eks_cluster.kubeconfig
)

# Create a deployment
app_labels = { "app": "demo-app" }
deployment = k8s.apps.v1.Deployment('demo-deployment',
    metadata={
        "name": "demo-app"
    },
    spec={
        "replicas": 2,
        "selector": {
            "matchLabels": app_labels
        },
        "template": {
            "metadata": {
                "labels": app_labels
            },
            "spec": {
                "containers": [{
                    "name": "demo-app",
                    "image": "paulbouwer/hello-kubernetes:1.10",  # Simple demo image
                    "ports": [{
                        "containerPort": 8080
                    }],
                    "resources": {
                        "requests": {
                            "cpu": "0.25",
                            "memory": "256Mi"
                        }
                    }
                }]
            }
        }
    },
    opts=pulumi.ResourceOptions(provider=k8s_provider)
)

# Create a service to expose the deployment
service = k8s.core.v1.Service('demo-service',
    metadata={
        "name": "demo-app"
    },
    spec={
        "type": "LoadBalancer",  # This will create an AWS ALB
        "ports": [{
            "port": 80,
            "targetPort": 8080
        }],
        "selector": app_labels
    },
    opts=pulumi.ResourceOptions(provider=k8s_provider)
)

# Export kubeconfig and the service URL
pulumi.export("kubeconfig", eks_cluster.kubeconfig)
pulumi.export("url", service.status.load_balancer.ingress[0].hostname)