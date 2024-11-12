import pulumi
import pulumi_awsx as awsx
import pulumi_eks as eks
import json

# Create VPC with default CIDR
eks_vpc = awsx.ec2.Vpc("eks-vpc",
    enable_dns_hostnames=True)

# Create minimal EKS cluster
eks_cluster = eks.Cluster("eks-cluster",
    vpc_id=eks_vpc.vpc_id,
    public_subnet_ids=eks_vpc.public_subnet_ids,
    private_subnet_ids=eks_vpc.private_subnet_ids,
    instance_type="t3.medium",
    desired_capacity=2,
    min_size=0,
    max_size=2,
    endpoint_public_access=True,
    tags={ "owner":"v-adam@pulumi.com"}
    )

# Export kubeconfig to stack output
pulumi.export("kubeconfig", eks_cluster.kubeconfig)