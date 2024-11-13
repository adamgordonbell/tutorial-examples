
Original:

Vid: https://www.youtube.com/watch?v=yA40w1ryMu8
https://www.pulumi.com/kubernetes/

Better version:

https://www.youtube.com/watch?v=wvUCZiRaX5w&list=PLyy8Vx2ZoWloyj3V5gXzPraiKStO2GGZw&index=8



# Demo: Deploying an EKS Cluster

Let's show a quick demo of how to deploy an AWS EKS cluster and an application into that cluster using Pulumi. We'll start by installing the package dependencies

-  pulumi new
- kubernetes-aws-python
- ca-central-1
- show clicking in
- copy in simplify exmaple
- show the code, click around, vpc, 
- show "    authentication_mode=eks.AuthenticationMode.API"
- Add
    tags={
        "managed-by":"pulumi",
        "owner":"v-adam@pulumi.com"
    },
    create_oidc_provider=True

- User installs dependencies (`npm install`)
- initializes stack (`pulumi stack init`), 
- sets region, 
- opens `index.ts`, 
- imports libraries, 
- writes VPC and EKS cluster code (using `pulumi preview` along the way), 
- exports `clusterKubeconfig`, deploys with `pulumi up`, 
- retrieves kubeconfig
- inspects nodes with `kubectl`.

…Great, everything's running.

# Expanding the Demo: Deploying a Pod

Let's expand the demo by deploying a new pod...

- User creates Kubernetes provider
- defines pod with Nginx container
- adds Debian sidecar
- deploys

We can check out its logs as well.


- checks pod status and logs with `kubectl`.

## IAC

so yeah, Pulumi is a modern infrastructure-as-code tool that allows you to declaratively describe and manage your infrastructure using your favorite programming language. You can use these programming languages to provision any AWS resource or GCP or Azure or lots more.

Any because its code, we can have tests, and IDE support and type checking And, most importantly, our SDKs are open source.

## More

So yeah, we can deploy cloud-native infrastructure and Kubernetes API resources through Pulumi. You can get started today by visiting pulumi.com. Thank you

---

My notes

-- he is using fargate
-- took 14 minutes to deploy

pulumi stack output kubeconfig > kubeconfig.json
export KUBECONFIG=`pwd`/kubeconfig.json
kubectl get nodes -o wide --show-labels
kubectl get pods -A


```
aws eks list-clusters --region ca-central-1
aws eks describe-cluster --name my-cluster --region ca-central-1
aws eks list-nodegroups --cluster-name my-cluster --region ca-central-1
aws ec2 describe-instances --region ca-central-1
aws elbv2 describe-load-balancers --region ca-central-1