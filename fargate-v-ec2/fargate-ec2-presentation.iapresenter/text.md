# Fargate vs EC2: Making the Right Choice
Welcome to this presentation about choosing between AWS Fargate and EC2 for your EKS workloads.
---
## What We'll Cover
- Understanding the key differences
- Bin packing and resource allocation
- Real-world use cases
- Cost considerations
- Making the right choice

These fundamentals will help you make an informed decision for your infrastructure.

---
## Simple Fargate Cluster Setup
```python
import pulumi
import pulumi_awsx as awsx
import pulumi_eks as eks

eks_cluster = eks.Cluster("eks-cluster",
    vpc_id=eks_vpc.vpc_id,
    private_subnet_ids=eks_vpc.private_subnet_ids,
    fargate=True,  
)
```
Setting up a Fargate cluster is straightforward with just a few lines of code.

---
https://www.pulumi.com/blog/fargate-vs-ec2/k9s-fargate.gif
size: contain

Notice how each pod gets its own dedicated node in Fargate.

---
## EC2 Cluster Setup
```python
eks_cluster = eks.Cluster("eks-cluster",
    vpc_id=eks_vpc.vpc_id,
    private_subnet_ids=eks_vpc.private_subnet_ids,
    instance_type="t3.medium",
    desired_capacity=2,
    min_size=1,
    max_size=2,
)
```
EC2 setup requires more configuration but offers greater control over instance types and scaling.

---
https://www.pulumi.com/blog/fargate-vs-ec2/k9s-eks.gif
size: contain

With EC2, pods are distributed across a smaller number of shared nodes.

---
https://www.pulumi.com/blog/fargate-vs-ec2/ec2-pods.png
size: contain
Title: EC2 Nodes
In EC2, Kubernetes must solve the bin-packing problem - fitting multiple pods across available nodes while optimizing resource usage.

---
https://www.pulumi.com/blog/fargate-vs-ec2/faregate-pods.png
size: contain
title: Fargate Nodes

Fargate simplifies this by providing a dedicated environment for each pod, eliminating the need for complex bin-packing decisions.

---
| Responsibility | EC2 | Fargate |
|----------------|-----|---------|
| Instance Types | You provision nodes | AWS provisions per pod request|
| Pod Isolation | You share resources per node | AWS isolates each pod |
| Resource Allocation | You find space on nodes | AWS creates dedicated space |

This shows the key differences in responsibilities between EC2 and Fargate approaches.

---
## Use Case: Static Analysis
---
https://www.pulumi.com/blog/fargate-vs-ec2/noisy.webp
title: noisy neighbor problem

- CPU-intensive batch jobs
- Memory requirements ~2GB per instance
- Bursty workload patterns
- Perfect for Fargate's isolation

---
## Use Case: E-commerce Microservices
---
https://www.pulumi.com/blog/fargate-vs-ec2/cash-register.webp
Title:Ecommerce Example

- Lightweight Go services
- Network-heavy operations
- Low CPU/memory requirements
- Ideal for EC2's resource sharing

---
## Cost Considerations
---
	- EC2: ~$0.01/hr per pod (t3.medium sharing)
	- Fargate: ~$0.025/hr per pod
	- Fargate Spot: Up to 70% cheaper
	- Consider operational overhead

While Fargate is more expensive per pod, consider the total cost including operational overhead and team capacity.

---
## Key Takeaways
---
	 Use EC2 for:
	  - Cost-sensitive workloads
	  - Resource sharing scenarios
	  - Fast pod startup time
---
	 Use Fargate for:
	  - Isolation requirements
	  - Bursty workloads


---
## Why Not Both?
---
	- EC2 for stable, predictable workloads
	- Fargate for isolation-sensitive tasks

Many organizations benefit from using both approaches where they make the most sense.

---
## Thank You!
Ready to streamline your EKS infrastructure?
Try Pulumi for infrastructure as code in your favorite programming language.