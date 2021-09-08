# Prerequesits - Access to kube config file
from kubernetes import client, config
config.load_kube_config()
Api = client.CoreV1Api()
print("Listing Servives with their Cluster IPs:")
result = Api.list_service_for_all_namespaces(watch=False)
for i in result.items:
    print("%s\t-%s\t-%s" % (i.metadata.namespace, i.metadata.name, i.spec.cluster_ip))