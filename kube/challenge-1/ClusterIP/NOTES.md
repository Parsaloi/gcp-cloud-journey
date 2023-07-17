
## Testing CluterIP service deployment

The first test to deploy a generic ClusterIP service to a k8s cluster was successful :)

- To deploy the service run:  
```bash
kubectl apply -f service.yaml
```
- To verify the service is deployed, run:  
```bash
kubectl get service
NAME        TYPE        CLUSTER-IP      EXTERNAL-IP     PORT(S)         AGE
service     ClusterIP   <cluster-addr>  <none>          80/TCP          3m35s
```
