import pulumi
import pulumi_awsx as awsx
import pulumi_eks as eks
import pulumi_kubernetes as k8s

# Create VPC with default CIDR
eks_vpc = awsx.ec2.Vpc("eks-vpc",
    enable_dns_hostnames=True)

# Create minimal EKS cluster
eks_cluster = eks.Cluster("eks-cluster",
    vpc_id=eks_vpc.vpc_id,
    private_subnet_ids=eks_vpc.private_subnet_ids,
    fargate=True,
)

# Create Kubernetes provider
k8s_provider = k8s.Provider('k8s-provider',
    kubeconfig=eks_cluster.kubeconfig
)

# Create a deployment
app_labels = { "app": "demo-app" }
deployment = k8s.apps.v1.Deployment('demo-deployment',
    metadata={"name": "demo-app"},
    spec={
        "replicas": 2,
        "selector": {"matchLabels": app_labels},
        "template": {
            "metadata": {"labels": app_labels},
            "spec": {
                "containers": [{
                    "name": "demo-app",
                    "image": "paulbouwer/hello-kubernetes:1.10",
                    "ports": [{"containerPort": 8080}]
                }]
            }
        }
    },
    opts=pulumi.ResourceOptions(provider=k8s_provider)
)

# Simple LoadBalancer service with minimal security annotations
service = k8s.core.v1.Service('demo-service',
    metadata={
        "name": "demo-app",
        "annotations": {
            # Just the essential security annotation
            "service.beta.kubernetes.io/aws-load-balancer-source-ranges": "0.0.0.0/0",
             "service.beta.kubernetes.io/aws-load-balancer-target-type": "ip",
        }
    },
    spec={
        "type": "LoadBalancer",
        "ports": [{
            "port": 80,
            "targetPort": 8080
        }],
        "selector": app_labels,
        "externalTrafficPolicy": "Local"

    },
    opts=pulumi.ResourceOptions(provider=k8s_provider)
)

pulumi.export("kubeconfig", eks_cluster.kubeconfig)
pulumi.export("vpc_id",eks_vpc.vpc_id)
# pulumi.export("url", pulumi.Output.concat("http://", service.status.load_balancer.ingress[0].hostname))