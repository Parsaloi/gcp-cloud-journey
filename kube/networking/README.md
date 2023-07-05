
# Creating a network and two subnets

1. In the host project, create a network names `shared-net`
2. Create two subnets named `tier-1` and `tier-2`
3. For each subnet, create two secondary address ranges: one for **Services**, and one for **Pods**

> *Note: The secondary address ranges for Pods, Services and nodes must not overlap 172.17.0.0/16 and must follow the defaults and limits for  
range sizes.* <https://cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#defaults_limits>

```gcloud
gcloud compute networks create shared-net \
--subnet-mode custom \
--project [HOST_PROJECT_ID]
```

In your new network, create a subnet named `tier-1`:  
```gcloud
gcloud compute networks subnets create tier-1 \
--project [HOST_PROJECT_ID] \
--network shared-net \
--range 10.0.4.0/22 \
--region us-central1 \
--secondary-range tier-1-services=10.0.32.0/20, tier-1-pods=10.4.0.0/14
```

Create another subnet named `tier-2`:
```gcloud
gcloud compute networks subnets create tier-2 \
--project [HOST_PROJECT_ID] \
--network shared-net \
--range 172.16.4.0/22 \
--region us-central1 \
--secondary-range tier-2-services=172.16.16.0/20, tier-2-pods=172.20.0.0/14
```

## Determining the names of service accounts in your service projects


