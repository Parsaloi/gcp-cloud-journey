
## Taint a node

```bash
kubectl taint nodes my-node key=value:taint-effect
```

In this example, replace `my-node` with the name of the node you want to taint, and set `key`, `value`, and `taint-effect` accordingly.  

> Adding tolerations to a Pod manifest
```YAML
apiVersion: v1
kinf: Pod
metadata:
  name: my-pod
spec:
  tolerations:
    - key: "key"
      value: "value"
      effect: "taint-effect"
```

The tolerations added to the Pod will allow it to be scheduled on the tainted node

## Taints and Tolerations
> <https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/>

*Node affinity* is a property of Pods that *attracts* them to a set of nodes (either as a preference or a hard requirement).  
***Taints*** are the opposite -- they allow a node t0 repel a set of pods.

***Tolerations*** are applied to Pods. *Tolerations* allow the scheduler to shedule pods with matching taints. Tolerations allow scheduling but don't  
guarantee scheduling: the scheduler also evaluates other parameters as part of its funtion

*Taints and tolerations* **work together** to ensure that Pods are not scheduled onto inappropriate nodes. One or more taints are applied to a node;  
this marks that the node should not accept any pods that do not tolerate the taints

### Concepts
You can add a taint to a node using `kubectl taint`. For example,  
```bash
kubectl taint nodes node1 key1=value1:NoSchedule
```
places a taint on a node `node1`. The taint has key `key1`, value `value1`, and *taint effect* `NoSchedule`. This means that no pod will be able to  
scehdule onto `node1` *unless it has a matching toleration*  

To remove the taint added by the command above, you can run:  
```bash
kubectl taint nodes node1 key1=value1:NoSchedule-
```

You specify a tol
