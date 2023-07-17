
## Instructions

1. To create the Pod:  
```bash
kubectl apply -f .yaml
```
2. Verify that the Pod's Container is running, and then watch for changes to the Pod:  
```bash
kubectl get pod test-redis --watch
#Example output is like...
NAME    READY   STATUS  RESTARTS    AGE
redis   1/1     Running 0           13s
```

*Extra*
3. In another terminal, get a shell to the running Container:
```bash
kubectl exec -it redis -- /bin/bash
```

4. In your shell, go to `data/redis`, and theb create a file:  
```bash
root@redis:/data# cd data/redis/
root@redis:/data/redis# echo Hello > test-file
```
