For springboot 3-tier project will this architecture plan work[Internet]
    |
    | (HTTPS/HTTP - Port 443/80)
    V
[Public Facing Frontend Load Balancer (ALB)]
    | (HTTP/HTTPS - e.g., Port 80/443 to Load Balancer)
    |
    V
[Private Subnet - Frontend EC2 Instances (Auto Scaling Group)]
    | (Internal HTTP - e.g., Port 8080 from Frontend to Backend LB)

