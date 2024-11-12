<!-- markdownlint-disable -->



#  Introducing Pulumi

**[0:00-0:19]**
* **Screen**: "pulumi" logo, "Modern Infrastructure as Code," description of language support, "What is Pulumi?" title card with bullet points (declaring infrastructure, provisioning resources, sharing best practices, previewing changes, auditing, secrets management, testing infrastructure), icons for Source Code/Languages/Tools, Python code snippet for AWS EC2.
* **Audio/Narration**: Pulumi is a modern infrastructure-as-code tool that allows you to declaratively describe and manage your infrastructure using your favorite programming language. We support JavaScript, TypeScript, Python, Go, and .NET. You can use these programming languages to provision any AWS resource or service that is offered. Because we have code, we can encapsulate this code to share best practices using package managers.


# Code-Based Infrastructure Management

**[0:19-0:52]**
* **Screen**: Focus on relevant bullet points ("Share best practices...", "Preview changes...", "Easy secrets management") and Python code snippet. Transitions to "Test your infrastructure" bullet point as the narration shifts to that topic.
* **Audio/Narration**: So we can use NPM if we're using node languages and we can use pip if we're using Python. Because we have code, we can see the preview of the changes that will happen before they take place and get a full audit of who changed what and when. We have built-in secret management support to protect the secrets that your infrastructure uses, along with the secrets that protect the state file for the stack itself in Pulumi. Because we have code, you can write unit tests and integration tests to validate and verify your infrastructure. And, most importantly, our SDKs are completely open source.


# Example: Creating AWS Resources

**[0:52-0:57]**
* **Screen**: Python code snippet is replaced with TypeScript code snippet for Kubernetes deployment.
* **Audio/Narration**: Here's an example of how to create an EC2 VM in a security group using the Python language.


# Managing Cloud-Native Services and Kubernetes

**[0:57-1:33]**
* **Screen**: "Kubernetes Superpowers" slide: title, "No YAML..." text, bullet points (declarative IaC, productivity, previewing changes, rich deployment status, Helm charts, sidecars, CI/CD integrations), TypeScript code snippet for Kubernetes deployment/service.
* **Audio/Narration**: Pulumi can also be used to manage Kubernetes as code, in addition to cloud-native services. That means you can use your favorite programming languages to describe your infrastructure, provision the API resources in Kubernetes, reduce the amount of copying and pasting you have to do, and benefit from the same preview changes and audit histories that you get with deploying cloud-native services. You can also deploy Helm charts, inject sidecars for Envoy, Istio, and others because it's just code. And we have many integration points with CI/CD systems. Here's an example of how to create a Kubernetes deployment and service using the TypeScript language in 33 lines of code.


# Demo: Deploying an EKS Cluster

**[1:33-2:54]**
* **Screen**: "Demo" slide, then two terminal windows.  User installs dependencies (`npm install`), initializes stack (`pulumi stack init`), sets region, opens `index.ts`, imports libraries, writes VPC and EKS cluster code (using `pulumi preview` along the way), exports `clusterKubeconfig`, deploys with `pulumi up`, retrieves kubeconfig, and inspects nodes with `kubectl`.
* **Audio/Narration**:  Let's show a quick demo of how to deploy an AWS EKS cluster and an application into that cluster. We'll start by installing the package dependencies…[continues as described in the previous detailed breakdown]…Great, everything's running.


# Expanding the Demo: Deploying a Pod

**[2:54-4:23]**
* **Screen**: Two terminal windows. User creates Kubernetes provider, defines pod with Nginx container, adds Debian sidecar, deploys, checks pod status and logs with `kubectl`.
* **Audio/Narration**: Let's expand the demo by deploying a new pod...[continues as described in the previous detailed breakdown]...We can check out its logs as well.


# Summary and Advanced Pulumi Features

**[4:23-5:00]**
* **Screen**: "More Ways to Use Pulumi" slide (abstractions, reusable components, IDE features), TypeScript code for ECS service, Go code for testing.  Transitions to final "pulumi" slide with call to action.
* **Audio/Narration**: As this demo showed, we can deploy cloud-native infrastructure and Kubernetes API resources through Pulumi...[continues as described in the previous detailed breakdown]...You can get started today by visiting pulumi.com. Thank you. 
