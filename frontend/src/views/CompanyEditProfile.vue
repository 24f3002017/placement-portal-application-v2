<template>

    <div class="d-flex flex-column min-vh-100">
    
        <CompanyNavbar/>
    
        <div class="container my-5 flex-grow-1">
    
            <h2 class="text-center mb-4">
    
                Edit Company Profile
    
            </h2>
    
            <div class="card shadow">
    
                <div class="card-body">
    
                    <div class="mb-3">
    
                        <label class="form-label">
    
                            Company Name
    
                        </label>
    
                        <input
                            class="form-control"
                            v-model="company.name"
                            disabled
                        >
    
                    </div>
    
                    <div class="mb-3">
    
                        <label class="form-label">
    
                            Email
    
                        </label>
    
                        <input
                            class="form-control"
                            v-model="company.email"
                            disabled
                        >
    
                    </div>
    
                    <div class="mb-3">
    
                        <label class="form-label">
    
                            Industry
    
                        </label>
    
                        <input
                            class="form-control"
                            v-model="company.industry"
                        >
    
                    </div>
    
                    <div class="mb-3">
    
                        <label class="form-label">
    
                            Website
    
                        </label>
    
                        <input
                            class="form-control"
                            v-model="company.website"
                        >
    
                    </div>
    
                    <div class="mb-3">
    
                        <label class="form-label">
    
                            HR Contact
    
                        </label>
    
                        <input
                            class="form-control"
                            v-model="company.hr_contact"
                        >
    
                    </div>
    
                    <div class="mb-3">
    
                        <label class="form-label">
    
                            Approval Status
    
                        </label>
    
                        <input
                            class="form-control"
                            v-model="company.approval_status"
                            disabled
                        >
    
                    </div>
    
                    <div class="text-center">
    
                        <button
                            class="btn btn-success me-2"
                            @click="updateProfile"
                        >
    
                            Save Changes
    
                        </button>
    
                        <button
                            class="btn btn-secondary"
                            @click="$router.back()"
                        >
    
                            Cancel
    
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

async function updateProfile(){

    try{

        const token = localStorage.getItem("token")

        const response = await axios.put(

            "http://127.0.0.1:5000/api/company/profile",

            {

                industry: company.value.industry,

                website: company.value.website,

                hr_contact: company.value.hr_contact

            },

            {

                headers:{

                    Authorization:`Bearer ${token}`

                }

            }

        )

        alert(response.data.message)

        router.push("/company/profile")

    }

    catch(error){

        if(error.response){

            alert(error.response.data.message)

        }

        else{

            alert("Server Error")

        }

    }

}

onMounted(()=>{

    fetchProfile()

})

</script>