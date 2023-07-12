
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
