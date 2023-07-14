### Kind Ingress (ingress.yaml)

Convention for naming - only CamelCase is for change:

    NAME                                            EXAMPLE
    SERVICE_NAME.NAMESPACE.svc.cluster.local    -   admin-svc-dev.dev.svc.cluster.local 
    SERVICE_NAME-svc-NAMESPACE                  -   admin-svc-dev
    LABEL_NAME-NAMESPACE                        -   admin-dev
    EXAMPLE_NAME-NAMESPACE                      -   admin-dev
    NAMESPACE                                   -   dev
    HOST                                        -   google.com
    SECRET_NAME-NAMESPACE-tls-secret            -   admin-dev-tls-secret