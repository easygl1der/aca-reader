"use client";

import { useEffect, useRef } from "react";

interface Node {
  id: string;
  x: number;
  y: number;
  vx: number;
  vy: number;
  radius: number;
  color: string;
  label: string;
  type: "core" | "branch" | "leaf";
}

interface Edge {
  source: string;
  target: string;
}

export default function AnimatedGraph() {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const rect = canvas.getBoundingClientRect();
    canvas.width = rect.width * 2;
    canvas.height = rect.height * 2;
    ctx.scale(2, 2);

    const width = rect.width;
    const height = rect.height;

    const nodes: Node[] = [
      // Core node (center)
      { id: "agi", x: width * 0.45, y: height * 0.45, vx: 0, vy: 0, radius: 22, color: "#6D28D9", label: "AGI", type: "core" },
      // Branch nodes
      { id: "alignment", x: width * 0.25, y: height * 0.25, vx: 0, vy: 0, radius: 18, color: "#7C3AED", label: "Alignment", type: "branch" },
      { id: "safety", x: width * 0.7, y: height * 0.22, vx: 0, vy: 0, radius: 16, color: "#8B5CF6", label: "Safety", type: "branch" },
      { id: "governance", x: width * 0.2, y: height * 0.6, vx: 0, vy: 0, radius: 17, color: "#06B6D4", label: "AI Gov", type: "branch" },
      { id: "policy", x: width * 0.75, y: height * 0.58, vx: 0, vy: 0, radius: 15, color: "#0EA5E9", label: "Policy", type: "branch" },
      // Leaf nodes
      { id: "superalignment", x: width * 0.1, y: height * 0.15, vx: 0, vy: 0, radius: 12, color: "#A78BFA", label: "Superalign", type: "leaf" },
      { id: "rlhf", x: width * 0.15, y: height * 0.38, vx: 0, vy: 0, radius: 10, color: "#C4B5FD", label: "RLHF", type: "leaf" },
      { id: "interpret", x: width * 0.35, y: height * 0.12, vx: 0, vy: 0, radius: 10, color: "#A78BFA", label: "Interp", type: "leaf" },
      { id: "eval", x: width * 0.55, y: height * 0.1, vx: 0, vy: 0, radius: 11, color: "#C4B5FD", label: "Eval", type: "leaf" },
      { id: "redteam", x: width * 0.85, y: height * 0.35, vx: 0, vy: 0, radius: 11, color: "#7DD3FC", label: "Red Team", type: "leaf" },
      { id: "blue", x: width * 0.9, y: height * 0.72, vx: 0, vy: 0, radius: 10, color: "#7DD3FC", label: "Blue Team", type: "leaf" },
      { id: "regulation", x: width * 0.88, y: height * 0.85, vx: 0, vy: 0, radius: 12, color: "#0EA5E9", label: "Reg EU", type: "leaf" },
      { id: "ethics", x: width * 0.08, y: height * 0.82, vx: 0, vy: 0, radius: 10, color: "#06B6D4", label: "Ethics", type: "leaf" },
      { id: "bias", x: width * 0.3, y: height * 0.75, vx: 0, vy: 0, radius: 9, color: "#A78BFA", label: "Bias", type: "leaf" },
    ];

    const edges: Edge[] = [
      { source: "agi", target: "alignment" },
      { source: "agi", target: "safety" },
      { source: "agi", target: "governance" },
      { source: "agi", target: "policy" },
      { source: "alignment", target: "superalignment" },
      { source: "alignment", target: "rlhf" },
      { source: "alignment", target: "interpret" },
      { source: "safety", target: "eval" },
      { source: "safety", target: "redteam" },
      { source: "policy", target: "blue" },
      { source: "policy", target: "regulation" },
      { source: "governance", target: "ethics" },
      { source: "governance", target: "bias" },
    ];

    const nodeMap = new Map(nodes.map((n) => [n.id, n]));

    let time = 0;
    let animationId: number;

    const draw = () => {
      time += 0.012;
      ctx.clearRect(0, 0, width, height);

      // Draw edges
      edges.forEach((edge) => {
        const source = nodeMap.get(edge.source);
        const target = nodeMap.get(edge.target);
        if (!source || !target) return;

        const pulse = 0.4 + Math.sin(time * 1.5 + edges.indexOf(edge) * 0.3) * 0.15;

        ctx.beginPath();
        ctx.moveTo(source.x, source.y);
        ctx.lineTo(target.x, target.y);

        const gradient = ctx.createLinearGradient(source.x, source.y, target.x, target.y);
        gradient.addColorStop(0, `${source.color}${Math.round(pulse * 255).toString(16).padStart(2, '0')}`);
        gradient.addColorStop(1, `${target.color}${Math.round(pulse * 255).toString(16).padStart(2, '0')}`);

        ctx.strokeStyle = gradient;
        ctx.lineWidth = 1.5;
        ctx.stroke();
      });

      // Draw nodes
      nodes.forEach((node, i) => {
        const floatX = Math.sin(time * 0.8 + i * 0.4) * 4;
        const floatY = Math.cos(time * 0.6 + i * 0.3) * 4;
        const pulse = 1 + Math.sin(time * 2 + i * 0.5) * 0.08;

        // Glow
        const glowGradient = ctx.createRadialGradient(
          node.x + floatX, node.y + floatY, 0,
          node.x + floatX, node.y + floatY, node.radius * 3.5
        );
        glowGradient.addColorStop(0, `${node.color}30`);
        glowGradient.addColorStop(0.5, `${node.color}10`);
        glowGradient.addColorStop(1, "transparent");
        ctx.fillStyle = glowGradient;
        ctx.beginPath();
        ctx.arc(node.x + floatX, node.y + floatY, node.radius * 3.5, 0, Math.PI * 2);
        ctx.fill();

        // Main circle
        const mainGradient = ctx.createRadialGradient(
          node.x + floatX - node.radius * 0.3,
          node.y + floatY - node.radius * 0.3,
          0,
          node.x + floatX,
          node.y + floatY,
          node.radius * pulse
        );
        mainGradient.addColorStop(0, node.type === "core" ? "#FFFFFF" : `${node.color}FF`);
        mainGradient.addColorStop(1, node.type === "core" ? "#F3F4F6" : `${node.color}CC`);

        ctx.beginPath();
        ctx.arc(node.x + floatX, node.y + floatY, node.radius * pulse, 0, Math.PI * 2);
        ctx.fillStyle = mainGradient;
        ctx.fill();

        // Border
        ctx.strokeStyle = node.color;
        ctx.lineWidth = node.type === "core" ? 3 : 2;
        ctx.stroke();

        // Label
        ctx.font = `${node.type === "core" ? "bold" : "500"} ${node.type === "core" ? 11 : 9}px Inter, system-ui`;
        ctx.fillStyle = node.type === "core" ? node.color : "#1F2937";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText(node.label, node.x + floatX, node.y + floatY + node.radius + 12);
      });

      animationId = requestAnimationFrame(draw);
    };

    draw();

    return () => {
      cancelAnimationFrame(animationId);
    };
  }, []);

  return (
    <canvas
      ref={canvasRef}
      className="w-full h-full min-h-[400px]"
      style={{ background: "linear-gradient(180deg, #F9FAFB 0%, #FFFFFF 100%)" }}
    />
  );
}
