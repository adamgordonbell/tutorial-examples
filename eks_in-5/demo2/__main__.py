import pulumi
import pulumi_awsx as awsx
import pulumi_eks as eks
import json

# Create VPC with default CIDR
# eks_vpc = awsx.ec2.Vpc("eks-vpc",
#     enable_dns_hostnames=True)

private_subnet_ids = ["subnet-005a8e4e9bd5693e8", "subnet-0026ea4731c376093", "subnet-0d297b70f33d5cd13"]


# Create minimal EKS cluster
eks_cluster = eks.Cluster("eks-cluster",
    vpc_id= "vpc-0efc11dc212a264d3",
    private_subnet_ids= private_subnet_ids,
    instance_type="t3.medium",
    desired_capacity=2,
    min_size=1,
    max_size=2,
    endpoint_public_access=True,
    node_associate_public_ip_address=False  # Ensure public IPs aren’t assigned
    )

# Export kubeconfig to stack output
pulumi.export("kubeconfig", eks_cluster.kubeconfig)