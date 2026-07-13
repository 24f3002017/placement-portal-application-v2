<template>

<nav
        class="navbar navbar-expand-lg"
        style="background-color: #7B1113;"
    >
    
        <div class="container">
    
            <router-link
                to="/company-dashboard"
                class="navbar-brand text-white fw-bold"
            >
                IIT MADRAS PLACEMENT CELL
            </router-link>
    
            <button
                class="navbar-toggler "
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#navbarNav"
            >
                <span class="navbar-toggler-icon"></span>
            </button>
    
            <div
                class="collapse navbar-collapse justify-content-end"
                id="navbarNav"
            >
    
                <ul class="navbar-nav align-items-center">
    
                    <li class="nav-item">
                        <router-link
                            to="/company-dashboard"
                            class="nav-link text-white"
                        >
                            Dashboard
                        </router-link>
                    </li>
    
                    <li class="nav-item">
                        <router-link
                            to="/company/create-job"
                            class="nav-link text-white"
                        >
                            Create Job
                        </router-link>
                    </li>
    
                    <li class="nav-item">
                        <router-link
                            to="/company/profile"
                            class="nav-link text-white"
                        >
                            Profile
                        </router-link>
                    </li>
    
                    <li class="nav-item ms-3">
                        <button
                            class="btn btn-danger btn-sm"
                            @click="logout"
                        >
                            Logout
                        </button>
                    </li>
    
                </ul>
    
            </div>
    
        </div>
    
    </nav>
    
    </template>
    
    <script setup>
    
    import { useRouter } from "vue-router"
    
    const router = useRouter()
    
    function logout(){
    
        localStorage.removeItem("token")
        localStorage.removeItem("role")
    
        router.push("/login")
    
    }
    
    </script>