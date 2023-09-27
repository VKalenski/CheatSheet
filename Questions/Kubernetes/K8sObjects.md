
https://www.vskills.in/practice/kubernetes-objects-questions

> 1. What characterizes DNS Label Names for Kubernetes object
- contain at most 63 characters
- contain only lowercase alphanumeric characters or '-'
- start and end with an alphanumeric character
- **All of these**

---

> 2. Select the field in the .yaml file, which stores version of the Kubernetes API you're using to create this object, if creating a Kubernetes object using kubectl
- **apiVersion**
- kind
- metadata
- spec

---

> 3. What characterizes namespaces in Kubernetes
- **virtual clusters**
- physical clusters
- virtual VMs
- physical VMs

---

> 4. Identify the field in the .yaml file, which stores what state you desire for the object, if creating a Kubernetes object using kubectl
- apiVersion
- kind
- metadata
- **spec**

---

> 5. Pick the field in the .yaml file, which has data that helps uniquely identify the object, including a name string, UID, and optional namespace, if creating a Kubernetes object using kubectl
- apiVersion
- kind
- **metadata**
- spec

---

> 6. Every Kubernetes object also has a _____ that is unique across your whole cluster.
- **UID**
- PID
- SID
- ID

---

> 7. What is not a characteristic of Kubernetes Labels
- They are key/value pairs attached to objects
- Labels are used to organize and to select subsets of objects.
- Labels can be attached to objects at creation time and subsequently added and modified at any time.
- **None of these**

---

> 8. Choose the field in the .yaml file, which stores what kind of object you want to create, if creating a Kubernetes object using kubectl
- apiVersion
- **kind**
- metadata
- spec