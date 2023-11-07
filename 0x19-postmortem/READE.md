Postmortem: Web Application Outage Incident
Issue Summary:
Duration:
Start Time: 2023-04-10 12:00 EAT (Makadara, Nairobi)
End Time: 2023-04-10 13:30 EAT (Makadara, Nairobi)

--Impact--:
● The outage affected the primary web application, which serves as the core platform for
our customers. During the incident, the service was completely unavailable.
● Approximately 75% of our users were unable to access the application, resulting in a
significant disruption to their operations.

--Root Cause--:
● The root cause was identified as a misconfigured load balancer that inadvertently
blocked incoming traffic to the application servers.

--Timeline--:
--Detection Time--:
2023-04-10 12:00 EAT (Makadara, Nairobi)
● The issue was initially detected by monitoring alerts, which reported a sudden drop in
traffic and high error rates.

--Actions Taken--:
● The operations team immediately initiated an investigation into the issue.
● Initially, we suspected a problem with the application servers and began examining logs
and performance metrics.
● As no issues were found at the application server level, we started looking into the
network layer, focusing on the load balancer.

--Misleading Investigation/Debugging Paths--:
● Initially, we spent time investigating application server logs and metrics, assuming the
issue was related to code changes.
● We considered potential DDoS attacks due to the sudden drop in traffic, which led us
down an unnecessary path of analyzing traffic patterns.
Escalation:
● As the investigation pointed towards a network-related issue, the incident was escalated
to the network engineering team and senior system administrators.
Resolution:
● We discovered that the primary load balancer had received a misconfiguration update,
causing it to block all incoming traffic. The misconfiguration inadvertently blacklisted the
IP ranges of our legitimate users.
● The issue was resolved by rolling back the load balancer's configuration to the last
known good state.
● Normal traffic flow was restored, and the web application became accessible to all
users.

--Root Cause and Resolution--:
--Root Cause--:
● The root cause of the outage was a misconfigured load balancer. The misconfiguration
led to the load balancer blocking incoming traffic from legitimate user IP ranges.
Resolution:
● The issue was resolved by reverting the load balancer's configuration to a previous
known-good state. We then implemented stricter change control procedures to prevent
similar misconfigurations in the future.

--Corrective and Preventative Measures--:
--Improvements/Fixes--:
● Implement stricter change control procedures for load balancer configurations to prevent
unauthorized or unintended changes.
● Enhance monitoring and alerting specifically for load balancer changes and
misconfigurations.
● Conduct a thorough review of incident response processes to improve detection,
escalation, and response times.

--Tasks to Address the Issue--:
● Implement a version control system for load balancer configurations to track changes
and enable rollbacks.
● Establish an incident response team with clearly defined roles and responsibilities.
● Conduct regular training sessions to educate staff about proper load balancer
configuration and best practices.

This incident highlighted the critical need for robust change control procedures, proactive
monitoring, and a well-defined incident response process. By implementing these corrective and
preventative measures, we aim to minimize the risk of similar outages in the future, ensuring a
more reliable and resilient service for our users.
