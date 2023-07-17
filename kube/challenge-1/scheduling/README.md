
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
