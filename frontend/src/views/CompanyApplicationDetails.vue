<template>

    <div class="d-flex flex-column min-vh-100">
    
        <CompanyNavbar />
    
        <div class="container my-5 flex-grow-1">
    
            <h2 class="text-center mb-4">
                Applicant Details
            </h2>
    
            <div class="card shadow">
    
                <div class="card-body">
    
                    <table class="table">
    
                        <tbody>
    
                            <tr>
                                <th width="30%">Name</th>
                                <td>{{ application.name }}</td>
                            </tr>
    
                            <tr>
                                <th>Roll Number</th>
                                <td>{{ application.roll_no }}</td>
                            </tr>
    
                            <tr>
                                <th>Email</th>
                                <td>{{ application.email }}</td>
                            </tr>
    
                            <tr>
                                <th>CGPA</th>
                                <td>{{ application.cgpa }}</td>
                            </tr>
    
                            <tr>
                                <th>Skills</th>
                                <td>{{ application.skills }}</td>
                            </tr>
                            <tr>
    <th>Resume</th>
    <td>
        <a
            v-if="application.resume"
            :href="`http://127.0.0.1:5000/uploads/resumes/${application.resume}`"
            target="_blank"
            class="btn btn-primary btn-sm"
        >
            View Resume
        </a>

        <span v-else class="text-muted">
            No Resume Uploaded
        </span>
    </td>
</tr>
<tr>
                    <th>Status</th>
                         <td>
                            <span class="badge bg-primary">
                                   {{ application.status }}
                            </span>
                        </td>

                </tr>
                           
    
                            <tr>
                                <th>Feedback</th>
                                <td>{{ application.feedback }}</td>
                            </tr>
    
                            <tr v-if="application.interview_date">
                                <th>Interview Date</th>
                                <td>{{ application.interview_date }}</td>
                            </tr>
    
                            <tr v-if="application.interview_time">
                                <th>Interview Time</th>
                                <td>{{ application.interview_time }}</td>
                            </tr>
    
                            <tr v-if="application.interview_mode">
                                <th>Interview Mode</th>
                                <td>{{ application.interview_mode }}</td>
                            </tr>
    
                            <tr v-if="application.interview_location">
                                <th>Interview Location</th>
                                <td>{{ application.interview_location }}</td>
                            </tr>
    
                        </tbody>
    
                    </table>
    
                    <div class="text-center mt-4">
    
                        <button
                            class="btn btn-success me-2"
                            v-if="application.status=='applied'"
                            @click="updateStatus('shortlisted')">
                            Shortlist
                        </button>
    
                        <button
                            class="btn btn-danger"
                            v-if="application.status=='applied'"
                            @click="updateStatus('rejected')">
                            Reject
                        </button>
    
                    </div>
    
                    <div
                        class="mt-4"
                        v-if="application.status=='applied'">
    
                        <label class="form-label">
                            Feedback
                        </label>
    
                        <textarea
                            class="form-control"
                            rows="3"
                            v-model="feedback"
                            placeholder="Enter feedback">
                        </textarea>
    
                    </div>
    
                    <div
                        class="card mt-4"
                        v-if="application.status=='shortlisted' && !interviewScheduled">
    
                        <div class="card-header text-center">
                            <h5>Schedule Interview</h5>
                        </div>
    
                        <div class="card-body">
    
                            <label class="form-label">
                                Interview Date
                            </label>
    
                            <input
                                type="date"
                                class="form-control mb-3"
                                v-model="interviewDate">
    
                            <label class="form-label">
                                Interview Time
                            </label>
    
                            <input
                                type="time"
                                class="form-control mb-3"
                                v-model="interviewTime">
    
                            <label class="form-label">
                                Interview Mode
                            </label>
    
                            <select
                                class="form-select mb-3"
                                v-model="interviewMode">
    
                                <option>Online</option>
                                <option>Offline</option>
    
                            </select>
    
                            <label class="form-label">
                                Meeting Link / Location
                            </label>
    
                            <input
                                type="text"
                                class="form-control mb-3"
                                v-model="interviewLocation">
    
                            <button
                                class="btn btn-primary"
                                @click="scheduleInterview">
    
                                Schedule Interview
    
                            </button>
    
                        </div>
    
                    </div>
    
                    <div class="text-center mt-4">
    
                        <button
                            class="btn btn-secondary"
                            @click="$router.back()">
    
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
import { useRoute } from "vue-router"
import axios from "axios"

const route = useRoute()

const application = ref({})

const feedback = ref("")

const interviewScheduled = ref(false)

const interviewDate = ref("")
const interviewTime = ref("")
const interviewMode = ref("Online")
const interviewLocation = ref("")

async function fetchApplication() {

    try {

        const token = localStorage.getItem("token")

        const response = await axios.get(

            `http://127.0.0.1:5000/api/company/application/${route.params.id}`,

            {

                headers: {

                    Authorization: `Bearer ${token}`

                }

            }

        )

        application.value = response.data

        if (response.data.interview_date) {

            interviewScheduled.value = true

        }

    }

    catch (error) {

        console.log(error.response)

    }

}

async function updateStatus(status) {

    if (!feedback.value.trim()) {

        alert("Please enter feedback before updating status.")

        return

    }

    try {

        const token = localStorage.getItem("token")

        await axios.put(

            `http://127.0.0.1:5000/api/company/application/${route.params.id}/status`,

            {

                status: status,

                feedback: feedback.value

            },

            {

                headers: {

                    Authorization: `Bearer ${token}`

                }

            }

        )

        feedback.value = ""

        fetchApplication()

    }

    catch (error) {

        console.log(error.response)

        alert(error.response.data.message)

    }

}

async function scheduleInterview() {

    if (!interviewDate.value ||
        !interviewTime.value ||
        !interviewMode.value ||
        !interviewLocation.value) {

        alert("Please fill all interview details.")

        return

    }

    try {

        const token = localStorage.getItem("token")

        await axios.put(

            `http://127.0.0.1:5000/api/company/application/${route.params.id}/status`,

            {

                interview_date: interviewDate.value,

                interview_time: interviewTime.value,

                interview_mode: interviewMode.value,

                interview_location: interviewLocation.value

            },

            {

                headers: {

                    Authorization: `Bearer ${token}`

                }

            }

        )

        alert("Interview scheduled successfully!")

        interviewScheduled.value = true

        fetchApplication()

    }

    catch (error) {

        console.log(error.response)

        alert(error.response.data.message)

    }

}

onMounted(() => {

    fetchApplication()

})

</script>