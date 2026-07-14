<template>

    <div class="d-flex flex-column min-vh-100">
    
        <CompanyNavbar/>
    
        <div class="container my-5 flex-grow-1">
    
            <h2 class="text-center mb-4">
    
                Company Profile
    
            </h2>
    
            <div class="card shadow">
    
                <div class="card-body">
    
                    <table class="table">
    
                        <tbody>
    
                            <tr>
    
                                <th width="30%">Company Name</th>
    
                                <td>{{ company.name }}</td>
    
                            </tr>
    
                            <tr>
    
                                <th>Email</th>
    
                                <td>{{ company.email }}</td>
    
                            </tr>
    
                            <tr>
    
                                <th>Industry</th>
    
                                <td>{{ company.industry }}</td>
    
                            </tr>
    
                            <tr>
    
                                <th>Website</th>
    
                                <td>{{ company.website }}</td>
    
                            </tr>
    
                            <tr>
    
                                <th>HR Contact</th>
    
                                <td>{{ company.hr_contact }}</td>
    
                            </tr>
    
                            <tr>
    
                                <th>Approval Status</th>
    
                                <td>
    
                                    <span
                                        class="badge"
                                        :class="company.approval_status=='approved'
                                            ? 'bg-success'
                                            : 'bg-warning text-dark'"
                                    >
    
                                        {{ company.approval_status }}
    
                                    </span>
    
                                </td>
    
                            </tr>
    
                        </tbody>
    
                    </table>
    
                    <div class="text-center mt-4">
    
                        <button
                            class="btn btn-warning me-2"
                            @click="$router.push('/company/profile/edit')"
                        >
    
                            Edit Profile
    
                        </button>
    
                        <button
                            class="btn btn-secondary"
                            @click="$router.back()"
                        >
    
                            Back
    
                        </button>
    
                    </div>
    
                </div>
    
            </div>
    
        </div>
    
    </div>
    
    </template>

<script setup>

import CompanyNavbar from "../components/CompanyNavbar.vue"

import { ref, onMounted } from "vue"

import { useRouter } from "vue-router"

import axios from "axios"

const router = useRouter()

const company = ref({})

async function fetchProfile(){

    try{

        const token = localStorage.getItem("token")

        const response = await axios.get(

            "http://127.0.0.1:5000/api/company/profile",

            {

                headers:{

                    Authorization:`Bearer ${token}`

                }

            }

        )

        company.value = response.data

    }

    catch(error){

        console.log(error.response)

    }

}

onMounted(()=>{

    fetchProfile()

})

</script>