# Best Buy Staff-Service

This is a simple cloud-native microservice built for Best Buy to manage staff records. It exposes REST APIs for creating, reading, updating, and deleting staff members.

## 📌 Functionality

- Create new staff members
- View existing staff details
- Update staff information
- Delete staff records

Data is stored in memory. The app follows 12-factor principles (env vars, statelessness, modular code).

## 🧪 API Endpoints

| Method | Endpoint           | Description              |
|--------|--------------------|--------------------------|
| POST   | `/staff`           | Create a new staff       |
| GET    | `/staff/{id}`      | Get staff by ID          |
| PUT    | `/staff/{id}`      | Update staff by ID       |
| DELETE | `/staff/{id}`      | Delete staff by ID       |

## 🐳 Docker

Docker image is available at:
[https://hub.docker.com/r/vaibhav2792/staff-service](https://hub.docker.com/r/<your-dockerhub-username>/staff-service)

## ☁️ Deployment

The service is deployed on Azure Kubernetes Service (AKS) using the `deployment.yaml` file.

## 🔄 CI/CD

Automated CI/CD pipeline is set up using GitHub Actions. On every `main` push:
- Builds and pushes Docker image
- Deploys updated service to AKS

## 🐞 Known Issues

- No persistence (in-memory only)
- Not production-secure (no auth, no logging, etc.)

## 👨‍💻 Developed By
Vaibhav Mishra
