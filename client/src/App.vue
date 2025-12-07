<script setup>
import HeroSection from './components/HeroSection.vue'
</script>

<template>
  <header class="header">
    <div class="logo">Lisandro<span class="dot">.</span></div>
    <nav>
      <a href="#about">About</a>
      <a href="#projects">Projects</a>
      <a href="#contact" class="cta">Contact</a>
    </nav>
  </header>

  <main>
    <HeroSection />
    
    <!-- Future Content -->
    <section id="about" class="container">
      <h2>About Me</h2>
      <p class="intro-text">
        Welcome to my digital playground. This site serves as a testbed for my latest experiments in web development and AI, 
        powered by a robust mid-tier Python backend and a sleek Vue.js frontend.
      </p>
    </section>
  </main>
  
  <footer>
    <p>&copy; 2025 Lisandro. Built with Vue & Flask.</p>
  </footer>
</template>

<style scoped>
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 2rem 4rem;
  backdrop-filter: blur(10px);
  position: fixed;
  width: 100%;
  top: 0;
  z-index: 100;
  border-bottom: 1px solid rgba(255,255,255,0.05);
}

.logo {
  font-family: var(--font-heading);
  font-size: 1.5rem;
  font-weight: 700;
  letter-spacing: -0.5px;
}

.dot {
  color: var(--color-primary);
}

nav {
  display: flex;
  gap: 2rem;
  align-items: center;
}

nav a {
  font-weight: 500;
  font-size: 0.95rem;
  color: var(--color-text-muted);
}

nav a:hover {
  color: var(--color-text);
}

nav a.cta {
  padding: 0.5rem 1.25rem;
  background: rgba(255,255,255,0.05);
  border: 1px solid var(--glass-border);
  border-radius: 20px;
  color: #fff;
  transition: var(--transition-smooth);
}

nav a.cta:hover {
  background: var(--color-primary);
  border-color: var(--color-primary);
  box-shadow: 0 0 15px var(--color-primary-glow);
}

main {
  padding-top: 80px;
}

.container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 4rem 2rem;
}

.intro-text {
  max-width: 600px;
  margin-top: 1rem;
  color: var(--color-text-muted);
  font-size: 1.1rem;
}

footer {
  text-align: center;
  padding: 2rem;
  color: var(--color-text-muted);
  font-size: 0.8rem;
  border-top: 1px solid var(--glass-border);
}

@media (max-width: 768px) {
  .header {
    padding: 1.5rem 2rem;
  }
  nav {
    display: none; /* simple mobile hide for now */
  }
}
</style>
