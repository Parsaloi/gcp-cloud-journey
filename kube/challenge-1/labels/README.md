
## Label Cluster Resources

To label cluster resources, you can use the `kubectl label` command or include the `metadata.labels` field in the resource manifest files.

```bash
kubectl lable deployment my-deployment app=my-app
```
This command adds the label `app: my-app` to the Deployment named `my-deployment`
