# Implicit Cloud Clone - Design Specification

## 1. Concept & Vision

**Purpose**: Clone the implicit.cloud marketing site and demo navigator interface - an AI knowledge base platform.

**Aesthetic Direction**: Enterprise SaaS with subtle sophistication - clean, professional, trustworthy. NOT generic "AI purple gradient" but rather a refined, editorial take with distinctive purple accents.

**Core Identity**:
- Premium enterprise feel without being cold
- Knowledge/wisdom undertones (subtle graph/network motifs)
- Trust and clarity over flashiness

## 2. Design Language

### Color Palette
```css
--color-primary: #6D28D9;        /* Deep purple - main brand */
--color-primary-light: #7C3AED;   /* Lighter purple for hover */
--color-primary-dark: #5B21B6;    /* Darker purple for active */
--color-accent: #06B6D4;         /* Cyan accent for highlights */
--color-bg-light: #F9FAFB;       /* Light gray sections */
--color-bg-dark: #111827;        /* Dark sections */
--color-text-primary: #1F2937;    /* Main text */
--color-text-secondary: #6B7280; /* Secondary text */
--color-text-light: #F9FAFB;     /* Light text on dark */
--color-border: #E5E7EB;         /* Subtle borders */
--color-card-bg: #FFFFFF;        /* Card background */
```

### Typography
- **Headlines**: "Instrument Sans" (Google Fonts) - bold, modern, distinctive
- **Body**: "Inter" - high readability (exception to rule: Inter is appropriate for body here)
- **Accent**: "JetBrains Mono" for code/technical elements

### Spatial System
- Section padding: 96px vertical (desktop), 64px (mobile)
- Container max-width: 1200px
- Grid: 12-column, 24px gap
- Card radius: 12px
- Button radius: 8px

### Motion Philosophy
- Entrance: Fade-up with stagger (opacity 0→1, translateY 20px→0, 500ms ease-out, 100ms stagger)
- Hover: Scale 1.02 + subtle shadow lift, 200ms
- Tab transitions: Smooth slide with fade, 300ms
- Scroll-triggered reveals via Intersection Observer

## 3. Layout & Structure

### Homepage Sections (in order)
1. **Navigation** - Sticky, blur backdrop, logo left, nav center, CTA right
2. **Hero** - Split layout: headline+CTA left (60%), animated graph demo right (40%)
3. **Feature Cards** - 3-column grid, icons + titles + descriptions
4. **Enterprise Tabs** - 6 tabs, each revealing content panel with illustration
5. **Testimonials** - Carousel with 6 quotes, dot navigation
6. **CTA Banner** - Dark gradient background, centered text + button
7. **Footer** - Multi-column links, minimal

### Navigator Page Sections
1. **Navigation** - Same as homepage
2. **Hero** - Title + description + framework badges
3. **Chat Demo** - Embedded iframe or simulated chat interface
4. **Example Questions** - List of 4 suggested queries
5. **CTA** - "Build Your Own Navigator" button
6. **Footer** - Same as homepage

## 4. Features & Interactions

### Navigation
- Sticky on scroll with backdrop blur
- Hover underline animation on nav items
- Dropdown on "Resources" (hover-triggered)
- Mobile: Hamburger menu with slide-in drawer

### Hero Section
- Animated graph visualization on right (SVG-based network animation)
- Staggered text reveal on load
- Primary CTA with hover glow effect

### Feature Cards
- Hover: Card lifts with shadow, icon scales slightly
- Icon: Custom SVG icons per feature

### Tab Interface
- Click switches tab with slide animation
- Active tab has purple underline indicator
- Content fades in on tab change

### Testimonial Carousel
- Auto-advance every 5 seconds (pauses on hover)
- Manual prev/next buttons
- Dot indicators (clickable)
- Smooth slide transition

### Chat Demo (Navigator)
- Simulated chat interface with example responses
- Message bubbles with avatar
- Suggested questions as clickable chips

## 5. Component Inventory

### Button
- **Primary**: Purple bg, white text, rounded, shadow on hover
- **Secondary**: Transparent, purple text, border on hover
- **States**: default, hover (lift+glow), active (darken), disabled (gray)

### Card
- White bg, subtle border, 12px radius
- Shadow: 0 4px 6px rgba(0,0,0,0.05)
- Hover: shadow increases, slight lift

### Tab
- Inactive: Gray text
- Active: Purple text + bottom border indicator
- Hover (inactive): Darker gray text

### Navigation
- Desktop: Horizontal links, CTA button
- Mobile: Hamburger → slide-in drawer

### Chat Bubble
- User: Right-aligned, purple bg, white text
- AI: Left-aligned, gray bg, dark text
- Rounded corners (16px)

## 6. Technical Approach

### Stack
- **Framework**: Next.js 14 (App Router) with TypeScript
- **Styling**: Tailwind CSS + custom CSS variables
- **Animations**: Framer Motion for complex, CSS for simple
- **Icons**: Lucide React

### Architecture
```
implicit-clone/
├── app/
│   ├── page.tsx              # Homepage
│   ├── navigator/
│   │   └── page.tsx          # Navigator demo page
│   ├── layout.tsx            # Root layout with nav/footer
│   └── globals.css           # Tailwind + custom styles
├── components/
│   ├── Navigation.tsx
│   ├── Hero.tsx
│   ├── FeatureCards.tsx
│   ├── EnterpriseTabs.tsx
│   ├── TestimonialCarousel.tsx
│   ├── CTABanner.tsx
│   ├── Footer.tsx
│   ├── ChatDemo.tsx
│   └── AnimatedGraph.tsx
├── lib/
│   └── utils.ts
├── public/
│   └── images/
├── tailwind.config.ts
├── next.config.js
└── package.json
```

### Key Implementation Details
- Use Framer Motion for page load animations
- Intersection Observer for scroll-triggered reveals
- CSS custom properties for theming
- Responsive: Mobile-first with breakpoints at 640px, 768px, 1024px, 1280px
