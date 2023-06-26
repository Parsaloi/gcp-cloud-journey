
# Deploying a stateless Linux application

## Overview

*Stateless applications* are applications which do not store data or application state to the ***cluster*** or to *persistent storage*.  
Instead, data and applications state stay with the client, which makes stateless applications more ***scalable***. For example, a frontend  
application is stateless:  
-  you deploy multiple replicas to increase availability and scale down when demand is low,  
- >  and the *replicas have no need for unique identies.*

Kubernetes uses the *Deployment* <https://kubernetes.io/docs/concepts/workloads/controllers/deployment/> controller to deploy stateless applications  
as *uniform*, *non-unique* ***Pods*** <https://kubernetes.io/docs/concepts/workloads/pods>. Deployments manage the *desired* state of your application:  
how many
