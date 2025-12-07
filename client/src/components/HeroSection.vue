<script setup>
</script>

<template>
  <section class="hero">
    <div class="hero-content">
      <div class="badge">Full Stack Engineer</div>
      <h1>
        Building <span class="gradient-text">Digital Experiences</span> that matter.
      </h1>
      <p class="subtitle">
        I create scalable, high-performance web applications with a focus on exceptional user experience and robust architecture.
      </p>
      <div class="actions">
        <a href="#projects" class="btn primary">View Projects</a>
        <a href="#about" class="btn secondary">Learn More</a>
      </div>
    </div>
    
    <div class="hero-image">
      <div class="image-wrapper">
        <img src="/lisandro-headshot.jpg" alt="Lisandro" />
        <div class="glow"></div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero {
  min-height: 90vh;
  display: flex;
  align-items: center;
  justify-content: center;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  gap: 5rem;
}

.hero-content {
  flex: 1;
  max-width: 600px;
  animation: fadeInUser 0.8s ease-out;
}

.badge {
  display: inline-block;
  padding: 0.5rem 1rem;
  background: rgba(99, 102, 241, 0.1);
  color: var(--color-primary);
  border-radius: 50px;
  font-size: 0.85rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
  border: 1px solid rgba(99, 102, 241, 0.2);
}

h1 {
  font-size: 4rem;
  line-height: 1.1;
  margin-bottom: 1.5rem;
  letter-spacing: -1px;
}

.gradient-text {
  background: linear-gradient(135deg, #fff 0%, var(--color-primary) 50%, var(--color-secondary) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.subtitle {
  font-size: 1.2rem;
  color: var(--color-text-muted);
  margin-bottom: 2.5rem;
  line-height: 1.7;
}

.actions {
  display: flex;
  gap: 1rem;
}

.btn {
  padding: 0.8rem 1.8rem;
  border-radius: 8px;
  font-weight: 600;
  transition: var(--transition-smooth);
}

.btn.primary {
  background: var(--color-primary);
  color: #fff;
  box-shadow: 0 4px 20px var(--color-primary-glow);
}

.btn.primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 30px var(--color-primary-glow);
}

.btn.secondary {
  background: rgba(255,255,255,0.05);
  color: #fff;
  border: 1px solid var(--glass-border);
}

.btn.secondary:hover {
  background: rgba(255,255,255,0.1);
  border-color: rgba(255,255,255,0.2);
}

.hero-image {
  flex: 1;
  display: flex;
  justify-content: center;
  animation: fadeInUser 1s ease-out 0.2s backwards;
}

.image-wrapper {
  position: relative;
  width: 380px;
  height: 480px;
  border-radius: 20px;
  overflow: hidden;
  border: 1px solid var(--glass-border);
  background: var(--glass-bg);
  box-shadow: var(--glass-shadow);
  transform: rotate(2deg);
  transition: var(--transition-smooth);
}

.image-wrapper:hover {
  transform: rotate(0deg) scale(1.02);
}

img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0.95;
}

.glow {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  background: linear-gradient(to bottom, transparent 60%, rgba(5,5,7,0.8));
  pointer-events: none;
}

@keyframes fadeInUser {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 968px) {
  .hero {
    flex-direction: column-reverse;
    text-align: center;
    padding-top: 4rem;
    gap: 3rem;
  }
  
  .hero-content {
    margin: 0 auto;
  }
  
  .actions {
    justify-content: center;
  }
  
  h1 {
    font-size: 3rem;
  }
  
  .image-wrapper {
    width: 300px;
    height: 380px;
    margin: 0 auto;
  }
}
</style>
