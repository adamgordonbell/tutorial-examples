Joe: And with Pulumi Insights, we're taking that to even the next level. Pulumi Insights applies intelligent Cloud management to give you instant visibility and control over all of your Cloud assets. It tames the chaos.

Craig: Thanks, Joe. So last year, we launched Insights 1.0 with the new resources page that helps you find and manage the resources in your infrastructure. Since then, we've heard great feedback from customers about the tools and updates they'd like to see. I'm happy to demo some of these improvements for you today.

The first update is that we have a significantly enhanced resources page to provide an updated layout as well as improvements for sorting and filtering directly from within the grid. We’ve also added the ability to group your resources by different columns so you can factor your infrastructure in different ways.

Grouping your resources helps you gain insights into your infrastructure and sometimes learn things you may not have expected. For example, having so many storage resources might be a surprise. Drilling in by module or stack could help you understand and manage those changes. You can also group by how resources are changing over time, making it easier to identify what stack caused the changes.

This new resources experience provides a flexible set of tools to help you understand and manage your infrastructure.

Pulumi CrossGuard and IaC already provide a flexible platform to ensure your infrastructure doesn’t introduce vulnerabilities, but we’ve taken this a step further. The new policy violations explorer allows you to browse all violations across your organization, sort and filter them, or group them by different criteria. For example, you can group violations by policy to identify recurring issues or by stack to locate where most issues exist and assign remediation work accordingly.

Knowing where the violations are is great, but fixing them is even better. The resource details page gives you the necessary information about policy violations and now includes a resource graph. This visual map shows resource dependencies and lets you drill down into related infrastructure, providing all the context you need to address violations effectively.

If you need to update IaC code to fix an issue, you can use the new Go to Definition link to jump straight to the relevant code for a resource, helping you resolve problems faster.

Finally, Pulumi Cloud now includes customizable dashboards to monitor your infrastructure comprehensively. You can create reports to track goals or progress over time. For example, here’s a resource count by category, giving a high-level overview of our infrastructure. Another card tracks progress on updating serverless applications to the latest Node.js runtime. Let’s add a new card to monitor EC2 volume usage for an ongoing project right-sizing volumes for each application. This enables you to track specific metrics as they evolve, all in one place.

Joe: Great demo, Craig! But there’s one last thing: What if all of this could work across any infrastructure—not just Pulumi IaC-managed resources, but Terraform, CloudFormation, or even manually provisioned infrastructure? Is that possible, Craig?

Craig: Well, I might just have a demo for that. Managing only IaC-managed resources is great, but not everyone has their infrastructure fully under Pulumi IaC management yet. To solve this, we’ve introduced account discovery, which leverages Pulumi’s open-source providers to scan and read resources from virtually every platform, including unmanaged ones.

With account discovery, Pulumi scans your account for resources not yet under IaC. Once we provide Pulumi the necessary account configuration, it starts scanning, dynamically adding unmanaged resources to the resource grid. This gives you visibility into your entire infrastructure—not just what’s managed by Pulumi.

You can use Pulumi Copilot to query even unmanaged resources. For example, asking, “Do I have any S3 buckets using standard storage?” Copilot identifies and returns the relevant results instantly. The dashboard also supports showing unmanaged resource details, letting you monitor their status alongside managed ones.

The policy violations explorer has also been extended to cover unmanaged resources. You can drill down into specific violations, view dependency graphs, and even get remediation suggestions. If you agree with the suggested fixes, Pulumi can directly apply changes to unmanaged infrastructure with full auditing.

Finally, to ensure future updates are robust, you can bring unmanaged resources into Pulumi IaC. Pulumi Cloud simplifies this process by identifying resource IDs and generating the code needed for import. This allows you to integrate those resources into IaC workflows and improve ongoing management.

With these updates, Pulumi Insights provides unparalleled visibility, control, and management tools for your entire infrastructure—whether managed with Pulumi, other IaC tools, or not managed at all.

Joe: That was amazing, Craig! Pulumi Insights 2.0 brings incredible innovation, offering visibility and management tools for all infrastructure, regardless of how it was provisioned.
