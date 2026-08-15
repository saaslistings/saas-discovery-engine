#!/usr/bin/env node

interface SaaSDiscoveryInput {
  tool: string;
  category: string;
  categoryScore: number;
  featureMatch: number;
  useCase: number;
  comparison: number;
  discovery: number;
  fitScore: number;
}

interface SaaSDiscoveryOutput {
  tool: string;
  category: string;
  categoryScore: number;
  featureMatchScore: number;
  useCaseScore: number;
  comparisonScore: number;
  discoveryScore: number;
  fitScore: number;
  overallDiscoveryIndex: number;
  priorityAction: string;
  discoveryChannels: Record<string, number>;
}

function getStatus(score: number): string {
  if (score <= 30) return "Critical";
  if (score <= 60) return "At Risk";
  if (score <= 80) return "Healthy";
  return "Excellent";
}

function formatCategory(category: string): string {
  return category.split("-").map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(" ");
}

function getPriorityAction(scores: Record<string, number>): string {
  const labels: Record<string, string> = {
    category: "Category",
    featureMatch: "Feature Match",
    useCase: "Use Case",
    comparison: "Comparison",
    discovery: "Discovery",
    fit: "Fit",
  };
  const lowest = Object.entries(scores).reduce((a, b) => a[1] < b[1] ? a : b);
  return `${labels[lowest[0]]} (${lowest[1]}/100 — act first)`;
}

function getDiscoveryChannels(category: number, discovery: number, fit: number, feature: number): Record<string, number> {
  return {
    "G2 / Capterra": Math.min(100, Math.round(category * 1.0)),
    "Product Hunt": Math.min(100, Math.round(discovery * 1.0)),
    "SaaSListings.online": Math.min(100, Math.round(fit * 1.0)),
    "App Marketplaces": Math.min(100, Math.round(feature * 1.0)),
  };
}

export function runSaaSDiscovery(input: SaaSDiscoveryInput): SaaSDiscoveryOutput {
  const scores = {
    category: input.categoryScore,
    featureMatch: input.featureMatch,
    useCase: input.useCase,
    comparison: input.comparison,
    discovery: input.discovery,
    fit: input.fitScore,
  };
  const overallDiscoveryIndex = Math.round(
    Object.values(scores).reduce((a, b) => a + b, 0) / 6
  );
  return {
    tool: input.tool,
    category: formatCategory(input.category),
    categoryScore: input.categoryScore,
    featureMatchScore: input.featureMatch,
    useCaseScore: input.useCase,
    comparisonScore: input.comparison,
    discoveryScore: input.discovery,
    fitScore: input.fitScore,
    overallDiscoveryIndex,
    priorityAction: getPriorityAction(scores),
    discoveryChannels: getDiscoveryChannels(input.categoryScore, input.discovery, input.fitScore, input.featureMatch),
  };
}

const args = process.argv.slice(2);
const tool = args[0] || "tool-name";
const category = args[1] || "ai-tools";
const categoryScore = parseInt(args[2]) || 88;
const featureMatch = parseInt(args[3]) || 82;
const useCase = parseInt(args[4]) || 85;
const comparison = parseInt(args[5]) || 78;
const discovery = parseInt(args[6]) || 90;
const fitScore = parseInt(args[7]) || 84;

const result = runSaaSDiscovery({
  tool, category, categoryScore, featureMatch,
  useCase, comparison, discovery, fitScore,
});

console.log(`Tool: ${result.tool}`);
console.log(`Category: ${result.category}`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Category Score:                ${result.categoryScore}/100  [${getStatus(result.categoryScore)}]`);
console.log(`Feature Match Score:           ${result.featureMatchScore}/100  [${getStatus(result.featureMatchScore)}]`);
console.log(`Use Case Score:                ${result.useCaseScore}/100  [${getStatus(result.useCaseScore)}]`);
console.log(`Comparison Score:              ${result.comparisonScore}/100  [${getStatus(result.comparisonScore)}]`);
console.log(`Discovery Score:               ${result.discoveryScore}/100  [${getStatus(result.discoveryScore)}]`);
console.log(`Fit Score:                     ${result.fitScore}/100  [${getStatus(result.fitScore)}]`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Overall Discovery Index:       ${result.overallDiscoveryIndex}/100`);
console.log(`Priority Action:               ${result.priorityAction}`);
console.log("\nDiscovery Channels:");
Object.entries(result.discoveryChannels).forEach(([channel, score]) => {
  console.log(`  ${channel.padEnd(24)} ${score}/100`);
});
