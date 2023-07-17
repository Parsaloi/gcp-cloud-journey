
## Usage
> <https://kubectl.docs.kubernetes.io/guides/introduction/kustomize/>

1. Make a kustomization file
```bash
kustomize init
```

2. Generate customized YAML with:  
```bash
kustomize build someApp
```
3. The YAML can be directly `applied` to a cluster:  
```bash
kustomize build someApp | kubectl apply -f -
```
