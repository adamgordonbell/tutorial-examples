
Vid: https://www.youtube.com/watch?v=yA40w1ryMu8
https://www.pulumi.com/kubernetes/

# Introduction to Pulumi

Pulumi is a modern infrastructure-as-code tool that allows you to declaratively describe and manage your infrastructure using your favorite programming language. We support JavaScript, TypeScript, Python, Go, and .NET. You can use these languages to provision any AWS resource or service.

# Code-Based Infrastructure Management

Because we use code, you can encapsulate best practices and share them using package managers like npm for Node.js and pip for Python. With code, you can preview the changes that will happen before they take place, and get a full audit of who changed what and when. Pulumi also has built-in secret management to protect both your infrastructure secrets and the state file itself.

# Testing Infrastructure

Since it's code, you can write unit and integration tests to validate and verify your infrastructure. Most importantly, our SDKs are completely open-source.

# Example: Creating AWS Resources

Here's an example of how to create an EC2 VM and a security group using Python.

# Managing Cloud-Native Services

Pulumi can also be used to manage cloud-native services like Kubernetes. This means you can describe your infrastructure, provision Kubernetes API resources, reduce repetitive configurations, and benefit from the same preview changes and audit history as with cloud-native deployments. You can also deploy Helm charts, inject sidecars like Envoy or Istio, and more. Pulumi integrates with many CI/CD systems.

# Advanced Deployments

Pulumi allows for advanced deployments, such as deploying Helm charts and injecting sidecars. We also have integration points with many CI/CD systems.

# Demo: Deploying AWS EKS Cluster

Let's do a quick demo. I'll deploy an AWS EKS cluster and an application to that cluster. First, I'll install the package dependencies needed for our program. Since I'm using TypeScript, I'll use npm. Once installed, we initialize our Pulumi stack, set the configuration (like the region to deploy into), and open our entry point, `index.ts`. We'll import all of the required SDK libraries.

We'll start by creating a VPC with public and private subnets across all availability zones in the region. My IDE provides autocomplete suggestions, which is a big help. I'll use standard CIDR block notation, and since it's code, I can easily reference documentation for more information.

Next, I'll specify the availability zones to use. Before creating the cluster, let's preview these changes. Everything looks good, so let's proceed. We'll create a new EKS cluster, bind it to the VPC's private subnets, and define it with a Fargate profile so that nodes are managed by Fargate. The preview looks good.

# Expanding the Demo: Deploying a Pod

Let's expand the demo by deploying a new pod. We'll create a provider, which is a wrapper for the kubeconfig that allows us to specify the cluster to use independently of the resources being deployed. We'll create a new pod with a sidecar, giving it a name and specifying the provider. If you've worked with Kubernetes, this spec will look familiar since we use the same API. We simply expose the Kubernetes OpenAPI spec as SDKs in the language of your choice.

We'll define the volume mounts for an Nginx container, and add a second container (a Debian container) to write to the shared pod volume. Once that's complete, we'll preview and update the changes to deploy the pod. When the pod is ready, we can examine it using `kubectl` and check the logs as well.

# Summary and Benefits

As this demo shows, Pulumi allows you to deploy both cloud-native infrastructure and Kubernetes API resources using real programming languages. This approach reduces boilerplate, allows for reusable components, and integrates well with existing tools and workflows. For example, our AWSX package makes it easy to describe a Fargate service with a load balancer.

You can use your IDE for linting, compilers for checking, and policy packs to catch issues before deployment. We even have an integration testing framework that allows you to test your Pulumi stacks using Go.

# Getting Started with Pulumi

Get started today by visiting pulumi.com. Thank you!

