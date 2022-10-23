# Primes as a Service

![cover image](./readme_assets/cover-image.png)  

## About
### Participants
* [Alex](https://github.com/pane2004)
* [Eugene](https://github.com/Ezzhingy)
* [Jerry](https://github.com/Bobliuuu)
* [Nathan](https://github.com/Nathan13888)
* [Vivian](https://github.com/vivian-dai)

### Description

Primes as a service is a medusa store for selling prime numbers for cryptography and RSA encryption. 

### Features
- Multiple types of primes offered
- Custom purchase and stripe checkout page
- Automated encrypted emails with your prime information
- 24/7 support and more! 

### Preview

<details>
<summary>Expand to see screenshots</summary>

![Home page](./readme_assets/prototype-primes.png)
![order](./readme_assets/order.png)
![products admin](./readme_assets/products.png)
![products client](./readme_assets/products-client.png)
![profile](./readme_assets/profile.png)
![purchase](./readme_assets/purchase.png)
![shipping](./readme_assets/shipping.png)
![emailed prime](./readme_assets/email.png)
</details>

## Setup
### Prerequisites
* [Node.js v14 or v16](https://nodejs.org)
* [Yarn](https://classic.yarnpkg.com/lang/en/docs/install/)
* [MinIO v8](https://min.io/)
* [Medusajs v15](https://medusajs.com/)

### Installation
Run `npm install` in the root folder, the `frontend` folder, and the `admin` folder  

Set up a Minio bucket, make it public and add `MINIO_ENDPOINT`, `MINIO_BUCKET`, `MINIO_ACCESS_KEY`, and `MINIO_SECRET_KEY` environment variables in the `.env` file. Check `.env.template` for what environment variables exist. `MINIO_ENDPOINT` is already configured in the `env.template`. Keep that. Refer to [Medusa.js's guide on setting up MinIO](https://docs.medusajs.com/add-plugins/minio/) for more information. 

Create a [Stripe](https://stripe.com) account and add your stripe API key as `STRIPE_API_KEY` in the `.env` file in root and your public key as `NEXT_PUBLIC_STRIPE_KEY` in the `.env` file in the [`frontend`](./frontend/) folder. This will be used for the Medusa checkout feature. 

### Running
Start MinIO:  
1. `./minio.exe server ./ --address 127.0.0.1:9001  --console-address :9090`  
Start Medusa in a new command line window:
2. `medusa develop`  
Open another instance of your command line to run frontend:
3. `cd frontend`
4. `yarn dev`  
Open yet another instance of your command line to run the admin:
5. `cd admin`
6. `npm start`

Your frontend should be running at http://localhost:8000/! 
Your medusa API is running at port 9000, and the admin portal is running at port 7000. 

### Backend

The backend of our app (prime generation) is a FastAPI endpoint hosted on Deta. 
You can test it out here: https://lpdet4.deta.dev/gentestprime
The docuentation is here: https://lpdet4.deta.dev/docs
An API key is required for production prime generation. 

To self host the FastAPI endpoint, run `uvicorn main:app --reload`, and see your app running at http://127.0.0.1:8000. 

An Azure VM hosts an email script to automate the prime checkout process. 

## Resources
* [Medusa's Github repository](https://github.com/medusajs/medusa)
* [Medusa Next.js Storefront](https://docs.medusajs.com/starters/nextjs-medusa-starter)
* [Medusa Admin](https://docs.medusajs.com/admin/quickstart/)
* [Medusa Minio](https://docs.medusajs.com/add-plugins/minio/)
* [Medusa Stripe](https://docs.medusajs.com/add-plugins/stripe/)
