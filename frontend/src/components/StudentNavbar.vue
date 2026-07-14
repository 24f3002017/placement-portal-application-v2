<template>

    <nav
        class="navbar navbar-expand-lg"
        style="background-color: #7B1113;"
    >

        <div class="container">

            <span class="navbar-brand text-white fw-bold">
                IIT Madras Placement Cell
            </span>

            <div class="ms-auto">

                <router-link
                    to="/student-dashboard"
                    class="btn btn-light btn-sm me-2"
                >
                    Dashboard
                </router-link>

                <button
                    class="btn btn-light btn-sm me-2"
                    @click="$router.push('/student/profile')"
                >
                    Profile
                </button>

                <button
                    class="btn btn-outline-light btn-sm"
                    @click="logout"
                >
                    Logout
                </button>

            </div>

        </div>

    </nav>

</template>

<script setup>

import { useRouter } from "vue-router"

const router = useRouter()

function logout() {
    localStorage.removeItem("token")
    localStorage.removeItem("role")
    router.push("/login")
}

</script>