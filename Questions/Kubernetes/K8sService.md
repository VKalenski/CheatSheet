
https://www.vskills.in/practice/kubernetes-service-questions

> 1. Which mode of finding a Service is supported by Kubernetes
- **environment variables and DNS**
- environment variables
- DNS.
- None of these

---

> 2. Which proxy mode involves kube-proxy to watch the Kubernetes master for the addition and removal of Service and Endpoint objects
- **User space proxy mode**
- iptables proxy mode
- IPVS proxy mode
- None of these

---

> 3. Select the proxy mode which involves kube-proxy to watch the Kubernetes control plane for the addition and removal of Service and Endpoint objects
- User space proxy mode
- **iptables proxy mode**
- IPVS proxy mode
- None of these

---

> 4. Why to use proxying for Services in Kubernetes
- There is a long history of DNS implementations not respecting record TTLs, and caching the results of name lookups after they should have expired.
- Some apps do DNS lookups only once and cache the results indefinitely.
- Even if apps and libraries did proper re-resolution, the low or zero TTLs on the DNS records could impose a high load on DNS that then becomes difficult to manage.
- **All of these**

---

> 5. Choose the proxy mode which involves kube-proxy watches Kubernetes Services and Endpoints and calls netlink interface
- User space proxy mode
- iptables proxy mode
- **IPVS proxy mode**
- None of these
