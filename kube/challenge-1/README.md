
## ClusterIP comments

This manifest creates a ClusterIP Service named `my-clusterip-service` that selects Pods with the label `app: my-app`. It exposes a `http` port `80` internally,  
forwarding traffic to the Pods on port `8080` targeting whichever host

### References
> <https://kubernetes.io/docs/concepts/services-networking/service/>

In *Kuberentes*, a **Service** is a method for exposing a network application that is running as one or more *Pods* in your cluster
