
> <https://kubernetes.io/docs/concepts/scheduling-eviction/pod-scheduling-readiness/>

## Pod Scheduling Readiness

**FEATURE STATE:** `Kubernetes v1.26 [alpha]`

Pods were considered ready for scheduling once created. Kubernetes scheduler does its due diligence to find nodes to place all pending Pods. However,  
in a real-world case, some Pods may stay in a "miss-essential-resources" state for a long period. These Pods actually churn the scheduler (and  
downstream integrators like *Cluster AutoScaler*) in an unecessary manner.

By specifying/removing a Pod's `.spec.schedulingGates`, you can control when a Pod is ready to be considered for scheduling

### Configuring Pod schedulingGates

The `schedulingGates` field contains a list of strings, and each string literal is perceived as a criteria that Pod should be satisfied before considered  
schedulable. This field can be initialized only when a Pod is created (either by the client, or mutated during admission). After creatinon, each  
*schedulingGate* can be removed in arbitrary order, but addition of a new scheduling gate is disallowed

## Pod Topology Spread Constraints

You can use ***topology spread contraints*** to control how Pods (A Pod represent a *set* of running containers in a cluster) are spread across your  
cluster among ***failure-domains*** such as *regions, zones, nodes, and other user-defined topology domains.* This can help to achieve **high  
availability** as well as **efficient resource utilization** <!--Awesome! :)-->

You can set ***cluster-level contraints*** as a default, or configure ***topology spread constraints*** for individual workloads

### Motivation
Imagine that you have a cluster of up to twenty nodes, and you want to run a workload (A workload is an application running on k8s) that automatically  
scales how many replicas it uses. There could be as few as two Pods or as many as fifteen. When there are only two Pods, you'd prefer not to have both  
of those Pods run on the same node...definetly...: you would run the risk that a single node failure takes your workload offline

In addition to this basic usage, there are some advanced usage examples that enable your workloads to benefit on **high availability** and   
**cluster utilization**

As you scale up and run more Pods, a different concern becomes important. Imagine that you have three nodes running five Pods each. The nodes have  
enough capacity to run that many replicas; however, the clients that interact with this workload are split across three different datacenters  
(or infrastructure zones). Now you have less concern about a single node failure, but you notice that latency is higher than you'd like, and you are  
paying for network costs associated with sending network traffic between the different zones

You decide that under normal operation you'd prefer to have a similar number of replicas schedules into each infrastructure zone, and you'd like the  
cluster to **self-heal** in the case that there is a problem.

Pod topology spread contraints offer you a declarative way to configure that.
