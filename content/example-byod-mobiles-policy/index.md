---
title: Government Cyber Security Policy – Bring Your Own Device (BYOD) Mobiles
summary: This policy sets out the limited circumstances in which government departments and their ALBs may permit employees to use their personally owned mobile phones and tablets to access, process or store limited, lower-risk corporate data under a BYOD model.
# Fill these in from the published page, then remove the # at the start.
# version: "1.0"
last_reviewed_on: 2025-06-10
# review_in: 12 months
---

# Government Cyber Security Policy – Bring Your Own Device (BYOD) Mobiles

> [!NOTE]
> This is a copy of the
> [BYOD mobiles policy](https://www.security.gov.uk/policy-and-guidance/policy/cyber-security-policy-bring-your-own-device-byod-mobiles/)
> on security.gov.uk, taken on 2026-10-28 to test the policy layout.

## Policy statement

1.1 This policy needs to be read in conjunction with the Government Security Group [“Corporate by Default” Device Deployment Policy](https://www.security.gov.uk/policy-and-guidance/policy/cyber-security-policy-corporate-by-default-device-deployment-policy/). The “Corporate by Default” policy mandates that by default users with a business need to access, process or store corporate data are provisioned with corporately owned and managed device(s) in favour of any other device deployment model.

1.2 Government organisations and their ALBs **may** permit employees to use their **personally owned mobile phones or tablets** to access, process or store **limited**, **lower-risk** corporate data under a Bring Your Own Device (BYOD) model in line with the requirements in this policy.

1.3 This policy applies to data at OFFICIAL.

1.4 This policy does not place any obligation on government organisations and their ALBs to deploy a BYOD model.


## Description

2.1 When an organisation is aware of and **actively manages** access to its data by employees’ personally owned devices, this is known as a Bring Your Own Device (BYOD) model.

2.2 BYOD must not be confused with “[Shadow IT](https://www.ncsc.gov.uk/guidance/shadow-it)”, or “grey IT”, which is when employees use devices or services which are unknown and unmanaged to access corporate data without active oversight by the organisation.

2.3 Employees’ personally owned devices pose unknown levels of cyber risk to corporate data, even when they are subject to some level of corporate management. At the same time, the measures available to actively manage employees’ personally owned devices to protect corporate data can pose a privacy risk to employees’ personal data. **Active oversight is required to balance any business benefits of a BYOD model against the inherent cyber security, data privacy and transparency risks**.

2.4 This document describes the technical and procedural controls that government organisations and their ALBs need to implement if they choose to deploy a BYOD model.


## Audience

3.1 This policy is intended for:

 - Security advisers responsible for the overall security of an organisation
 - Chief Digital and Information Officers and/or Chief Technology Officers responsible for funding and maintaining the organisation’s corporate IT
 - Cyber security professionals responsible for advising technical teams on the secure management of IT assets and infrastructure
 - Technical delivery teams responsible for managing IT assets and infrastructure


## Scope

### Organisations

4.1 This policy applies to government organisations and their ALBs.

### Devices and data

4.2 This policy applies to employees’ personally owned mobile phones and tablets when used to access, process or store corporate data.

4.3 This policy applies to data at OFFICIAL.

### Users

4.4 BYOD **shall not** be used for anyone in scope of the Government Security Group (GSG) [VIP Mobile Phones Policy](https://www.security.gov.uk/policy-and-guidance/policy/cyber-security-policy-vip-mobile-phones-policy/). This means Cabinet ministers, permanent secretaries, junior ministers, senior officials, Private Offices and individuals in other critical roles deemed to be higher risk at the organisation’s discretion (for example, special advisers and those working in National Security roles).

For these users, government organisations and their ALBs **shall** apply the specific COPE solution (Corporately Owned, Personally Enabled) in the [GSG VIP Mobile Phones Policy](https://www.security.gov.uk/policy-and-guidance/policy/cyber-security-policy-vip-mobile-phones-policy/), using the GSG VIP Mobile Technical Pattern.

We advise you to contact your security team in your organisation for more information on how the [GSG VIP Mobile Phones Policy](https://www.security.gov.uk/policy-and-guidance/policy/cyber-security-policy-vip-mobile-phones-policy/) is being implemented locally.

4.5 Not all of the requirements in this policy will automatically be suitable in relation to third-party suppliers contracted by government organisations or their ALBs. Third-party suppliers might be from a large organisation using a third-party’s corporately owned and managed enterprise IT, or they might be a sole trader using their personally owned device to run their business.

For these users, government organisations and their ALBs **shall**:

 - make an assessment of the sensitivity and business criticality of the corporate data in scope, the security standard of the third-party supplier’s IT, and the value for money; and
 - based on the above assessment, **either** impose bespoke security requirements via contractual terms and conditions and/or Security Aspect letters, **or** provision a corporate solution in line with the [Mobile Device Management (MDM) policy](https://www.security.gov.uk/policy-and-guidance/policy/government-cyber-security-policy-mobile-device-management/).


## Risks addressed

5.1 Data breaches of employees’ personally owned devices pose the following risks:

 - risk of reputational damage to government organisations, ALBs and/or the individuals affected
 - legal liability for government organisations, ALBs and/or the individuals affected
 - negative impacts on the rights, freedoms and safety of private individuals
 - negative impacts on the operation of government and ALBs’ essential functions and delivery of public services


## Policy requirements

This policy contains both mandatory and advisory elements, using the same language as [Functional Standard GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security):

 - **shall** means a requirement: a mandatory element
 - **should** means a recommendation: an advisory element
 - **may** means approval

6.1 Government organisations and their ALBs **may** permit employees to use their personally owned **mobile phones or tablets** to access, process or store **limited**, **lower-risk** corporate data under a Bring Your Own Device (BYOD) model in line with the requirements in this policy.

6.2 This policy does not place any obligation on government organisations and their ALBs to deploy a BYOD model.

### General best practice requirements

Government organisations and ALBs deploying a BYOD model **shall**:

 - 6.3 implement this policy in consultation with the organisation’s data protection advisers, legal advisers and knowledge and information management team (or equivalent).
 - 6.4 undertake a Data Protection Impact Assessment (DPIA) in order to identify and minimise risks to employees’ personal data when using their personally owned devices for work purposes.
 - 6.5 include the implementation of a BYOD model in the organisation’s formal governance and risk management processes.

### Requirements for determining business need and managing who has BYOD access

Government organisations and ALBs deploying a BYOD model **shall**:

6.6 Have a process in place for business units to request approval for each new BYOD use case. A proposed use case for BYOD **should** be a specific and clearly defined work activity, time-limited project, job role or business unit.

6.7 Only permit BYOD access to corporate data for use cases which have been approved by the Senior Officer accountable for security in the organisation (or person with delegated authority) following a formal review and risk assessment process. The purpose of the formal review and risk assessment process is to ensure that BYOD is not used in higher-risk use cases and to minimise the amount of corporate data exposed to employees’ personally owned devices.

6.8 Formally review and risk assess each proposed use case for BYOD, taking into consideration:

 - the business need and cost-benefit analysis for a BYOD solution, including justification as to why this need cannot be met by a fully corporately owned and enabled solution or a COPE solution
 - the minimum amount of corporate data which is strictly necessary for employees to access in order to meet the specified business need
 - the sensitivity and business criticality of the corporate data in scope – this includes the potential impacts if this data were lost or compromised and its potential value to a malicious actor
 - the threat posed to the job roles or the specific individuals in scope – this includes employees’ responsibilities within the organisation, the subject matter that they deal with, and whether this could make them of interest to a malicious actor
 - advice from the organisation’s data protection advisers, legal advisers, and knowledge and information management team (or equivalent)

6.9 Have a process in place for onboarding employees’ personal devices for BYOD use cases which have been approved by the Senior Officer (or person with delegated authority).

6.10 Have a process in place for business units to report changes in their BYOD business requirements. For example, if access to additional corporate data or by additional employees is required, or if access is no longer required.

6.11 Have a process in place for previously approved BYOD use cases to be re-reviewed by the Senior Officer (or person with delegated authority) if business requirements change.

6.12 Have a process in place for offboarding employees’ personal devices and shutting down BYOD use cases when access to corporate data is no longer required or Senior Officer approval is withdrawn.

6.13 Understand the aggregate risk to corporate systems and data across all permitted BYOD use cases in the organisation, not just each individual BYOD use case in isolation.

6.14 Maintain a record of use cases approved for BYOD and review this list on a regular basis, at least annually.

**Note**: The Senior Officer (or person with delegated authority) **may** revoke approval for a BYOD use case which was previously approved as they see fit – for example, if the risks posed to corporate data or the organisation’s risk appetite have changed.

6.15 Identify and catalogue all employees’ personally owned devices with access to corporate data as part of the organisation’s asset management process.

### Requirements for managing which corporate data is exposed to BYOD access:

Government organisations and ALBs deploying a BYOD model **shall**:

6.16 Only permit BYOD access to the minimum amount of corporate data which is strictly necessary for employees to access in order to meet the identified business need – this is known as the “principle of least privilege”.

For example:

 - specific files or folders, not the full organisational document library
 - specific records or data points, not the complete dataset
 - an individual mailbox
 - an individual calendar
 - low sensitivity corporate intranet pages, not the full corporate intranet
 - specific applications or functionality, such as to join virtual meetings, view payslips, claim expenses, report absences or undertake mandatory e-learning
 - (This is not an exhaustive list.)

6.17 Only expose constrained versions of the required corporate resources to employees’ personally owned devices, to enable employees to perform specific tasks or view specific information but not to connect into the internal corporate network.

6.18 Prevent privileged access occurring from any employee personally owned device. For example, employees’ personally owned devices **shall not** be permitted access to “backend” configuration controls or to perform administration or maintenance functions.

### Requirements for enforcing minimum security standards for BYOD devices:

Government organisations and ALBs deploying a BYOD model **shall**:

6.19 Define a compulsory “secure baseline build” of at least the security standard aligned to the organisation’s overarching security policies, specifying which device platform(s), minimum security version(s) and configuration(s) are permitted to access corporate data under a BYOD model.

**Note**: Not all device platforms, security versions and configurations offer the same technical controls and not all will be able to meet the requirements described in this policy, or provide an acceptable level of security against the OFFICIAL threat model. Further information on the OFFICIAL threat model is available in the Government Security Classifications Policy [Guidance 1.5 – Considerations for Security Advisers](https://assets.publishing.service.gov.uk/media/649c392a06179b00113f7464/Guidance_1.5__Considerations_for_Security_Advisors.pdf).

6.20 Include in the definition of “secure baseline build” that the device operating systems, firmware and apps will be supported by the manufacturer/developer for the entire duration of the device’s expected lifetime.

6.21 Formally review and update the defined secure baseline build required for BYOD access to corporate data on a regular basis, at least annually.

### Requirements for active technical management of BYOD devices:

Government organisations and ALBs deploying a BYOD model **shall**:

6.22 Apply appropriate technical controls and appropriately configure native apps to **segregate corporate data on the employee’s personally owned device**. For example, within a **corporately managed** app or container.

6.23 Implement technical controls to limit access to corporate networks and information systems to employees’ personally owned devices which are authorised, authenticated, up-to-date, patched and compliant with policy.

6.24 **Not** enrol employees’ personally owned devices onto their standard full corporate [Mobile Device Management (MDM)](https://www.security.gov.uk/policy-and-guidance/policy/government-cyber-security-policy-mobile-device-management/) solution, as this would give the organisation an unacceptable level of access to employees’ personal data held on the device and could also introduce the risk of accidentally wiping or otherwise harming the device.

6.25 Only permit BYOD access to corporate data to a corporately managed app/container on an employee’s personally owned device which has been configured or subject to technical controls as follows:

 - Requires strong authentication, such as phishing-resistant authentication Multi-Factor Authentication (MFA), anywhere that credentials can be used to access corporate resources.
 - Is secured with a passcode/PIN and/or biometric authentication, such as fingerprint or facial recognition. This is to ensure that access to corporate data from the device is exclusively by the employee only, not by any other person who may also use the device or have access to it.
 - Ensures corporate data is protected in transit between corporate networks and information systems and employees’ personally owned devices.
 - Prevents corporate data being copied and pasted, or otherwise captured and shared, from the corporately managed app/container to the non-corporately-managed parts of the employee’s personal device or to another device.
 - Prevents corporate data from being backed-up to non-corporately-managed applications, services, accounts and app stores, or synced with the non-corporately-managed parts of the employee’s personal device, such as the employee’s personal calendar appointments, photos, files and emails.
 - Prevents employees’ personal data from being backed-up to corporate data stores or synced with the corporate parts of the device. This includes implementing technical controls to manage which permissions corporate apps can request and configuring them to prevent corporate apps from accessing employees’ personal data. For example, employees’ personal calendar appointments, photos, files and emails.
 - Corporate apps on the employee’s personal device comply with the relevant requirements in the government [Mobile Device Management (MDM) policy](https://www.security.gov.uk/policy-and-guidance/government-cyber-security-policy-mobile-device-management/).

6.26 Implement technical controls which prohibit employees from removing or weakening the controls over the corporately managed app/container on their personally owned device.

6.27 Implement logging and monitoring controls **over the corporately managed app/container only** to achieve an equivalent level of logging and monitoring as on a fully corporately owned and enabled device.

6.28 Collect the following logging and monitoring data from the corporately managed app/container and scan for indicators of compromise (where technically possible and in compliance with the relevant provisions in the UK GDPR and the Data Protection Act 2018 to protect employees’ privacy):

 - events in the corporately managed parts of the device, including user activity, network communications, authentication, and access to corporate networks and information systems
 - apps installed in the corporately managed parts of the device, including the presence of unauthorised apps where this information is available

6.29 Implement “read only” “yes/no” compliance checks which **only collect device data which does not impact on the employee’s privacy** where the decision to permit BYOD access requires the organisation to understand the settings, status or configuration of the employee’s personally owned device outside of the corporately managed app/container.

For example:

 - whether the employee has enabled a passcode/PIN or biometric authentication on their device
 - whether the device is reporting itself as being free from malware
 - whether the device has identified that it has been “jailbroken” or “rooted” (this means if someone has removed the controls intentionally put in place by the device manufacturer to prevent the user from having full privileged access rights over their device)
 - (This is not an exhaustive list.)

6.30 Maintain the ability to revoke access to corporate data by employee’s personally owned devices.

6.31 Where technically possible, maintain the ability to enforce a remote wipe of the corporately managed app/container.

### Requirements to provide guidance and ensure that employees understand their rights and responsibilities:

Government organisations and ALBs deploying a BYOD model **shall**:

6.32 Maintain an Acceptable Use Policy (AUP) to ensure that employees understand the behaviours they need to adopt, any actions they need to take and what their security responsibilities are when accessing corporate data using their personally owned device(s).

6.33 Issue BYOD guidance for employees to support implementation of this policy. BYOD guidance **should** include information for employees on:

 - what to do if their business requirements change, for example they need to access additional corporate data or no longer require any access
 - the offboarding process for access to corporate data to be revoked, including how to remove any remaining corporate data and return their personally owned device to its previous state
 - how to report if their personally owned device is lost or stolen, or is no longer in their possession for another reason (for example – sent away for repair, lent to someone they know, sold to a third party)
 - how to report problems accessing corporate data and get IT support
 - how to raise a request for new features or functionality for the corporately managed app/container
 - what to do if they want to revert to a fully corporate solution because they no longer wish to use their personally owned device for work purposes
 - how organisational policy on use of corporate devices overseas applies to the BYOD-enabled device (see section 6.39 – 6.41 below)
 - how to update and patch their personally owned device operating system, firmware and apps according to best practice
 - how to protect against phishing
 - how to avoid downloading untrusted or unverified apps, or otherwise inadvertently downloading malware on their device
 - how to raise concerns about maintaining a healthy work-life balance when using their personal device(s) for work purposes and get wellbeing support
 - (This is not an exhaustive list.)

6.34 Issue employees in scope with a Privacy Notice which clearly sets out how their personal data may be used under a BYOD model and their rights. This includes:

 - how their device will be technically managed whilst it is being used for work purposes
 - how personal data held on the device may be logged, monitored, inspected, copied for the purposes of the public record, or otherwise processed whilst the device is being used for work purposes
 - how personal data held on the device may be used in the event that their device is suspected to have been involved in a cyber security incident or data breach affecting the organisation (see sections 6.42 – 6.44 below)
 - how personal data held on the device may be used in relation to a statutory request for information (such as under the Freedom of Information Act 2000, or a subject access request under UK GDPR) or in the course of an investigation, inquiry or in relation to litigation (see sections 6.45 – 6.47 below)
 - a point of contact for users if they have concerns or questions regarding how personal data held on their device will be processed

### Equalities requirements

6.35 It is expected that organisations’ corporate technology offering is fit-for-purpose and that employees with protected characteristics (such as disabilities or health conditions) are not put at a disadvantage when using corporately owned and managed technology. At the same time, individuals with disabilities or health conditions might actively want to use their personal device(s) for business purposes, for example if their personal device is specially configured to meet their needs or is running specialist accessibility tools.

6.36 If an employee requests to use their personal device(s) for business purposes as a reasonable workplace adjustment under the Equality Act 2010, this use case **shall** be subject to the formal review and risk assessment as set out at sections 6.6 – 6.8 above.

6.37 If this use case is not approved by the Senior Officer (or person with delegated authority) following formal review and risk assessment, the organisation **shall** work with their HR team and, where appropriate, Employment Group in Government Legal Department to find an alternative reasonable adjustment which mitigates the identified disadvantage.

6.38 Government organisations and ALBs which limit or ban use of BYOD **shall** complete a Public Sector Equality Duty (PSED) analysis of the impact on individuals with protected characteristics, such as individuals with disabilities or health conditions.

### Use of BYOD devices overseas

6.39 If an employee’s personal device has been BYOD-enabled, for example if it has a corporately managed app or container configured, then corporate data is present on that device.

6.40 For the purposes of determining whether an employee is permitted to take their BYOD device overseas, **either for personal use or business use**, the BYOD device **shall** be treated like any corporately owned device in line with the organisation’s existing policy on use of corporate devices overseas.

6.41 If under the organisation’s existing policy the employee is **not** permitted to take their BYOD device overseas, then the government organisation or ALB **shall** complete the offboarding process for access to corporate data to be revoked and return the device to its previous state within reasonable timescales before the employee travels overseas.

### Cyber security incidents or data breaches involving BYOD devices

6.42 It is expected that the logging and monitoring controls over the corporately managed app/container are sufficient to assist an incident investigation, as with a fully corporately owned and enabled device – see section 6.27 above.

6.43 In the event that a BYOD device is suspected to have been involved in a cyber security incident or data breach affecting the organisation, government organisations and their ALBs **shall**:

 - limit any inspection and analysis of the device to the corporately managed app/container only
 - carry out any inspection and analysis of the corporately managed app/container remotely, without requiring the employee to physically hand over their device

6.44 **In exceptional circumstances only**, the organisation **may** request the employee’s express and informed consent to voluntarily provide access to their device to enable inspection of the corporately managed app/container – for example, if remote inspection of the corporately managed app/container is not technically possible due to the device’s architecture. The employee **may** refuse this request at their discretion.

### Information access requests for corporate data held on BYOD devices

6.45 An information access request could be a statutory request for information (such as under the Freedom of Information Act 2000, or a subject access request under UK GDPR) or in the course of an investigation, inquiry or in relation to litigation.

6.46 Information access requests made in relation to corporate data held in the corporately managed app/container **shall** be treated like any other such request for corporate data held on a corporate system.

6.47 If an information access request is made in relation to corporate data held in the user-managed parts of the device, then the Cabinet Office guidance on use of non-corporate communication channels (NCCCs) applies – see the section of that guidance on “Transparency considerations”. For example, if the employee has used a non-corporate communication channel such as WhatsApp or their private email to carry out government business in the user-managed parts of the device


## Implementation and compliance

7.1 Organisations **shall** ensure a threat-driven, risk-based approach to implementation, proportionate to the prevailing level of cyber risk, within practicable timescales, and in line with their organisation’s business objectives and priorities. This means that organisations have the flexibility to decide how to meet the requirements of this policy in practice.

7.2 Where an organisation is not compliant with the requirements of this policy, this risk **shall** be formally managed and the appropriate risk mitigations put in place in line with the organisation’s risk tolerance.

7.3 Organisations **should** have a plan in place to work towards future compliance with this policy, in a way that meets their business objectives and priorities and to ensure continuous improvement over time.


## Supporting material and standards

8.1 This policy is supported by and relates to:

 - [Functional Standard GovS 007: Security](https://www.gov.uk/government/publications/government-functional-standard-govs-007-security), which sets expectations for what security activities organisations need to carry out and why in order to protect government assets
 - The [Cyber Security Standard](https://www.security.gov.uk/policy-and-guidance/the-cyber-security-standard/), which sets out how organisations need to do this in relation to cyber security, specifying the particular procedures organisations need to follow and the performance criteria to be met
 - Cabinet Office guidance on use of [non-corporate communication channels (NCCCs)](https://www.gov.uk/government/publications/non-corporate-communication-channels-for-government-business) such as as WhatsApp or private email for government business from an employee’s personally owned device
 - Government Security Group [Mobile Device Management (MDM) Policy](https://www.security.gov.uk/policy-and-guidance/government-cyber-security-policy-mobile-device-management/) on the secure management of corporately owned devices
 - Government Security Group [VIP Mobile Phones Policy](https://www.security.gov.uk/policy-and-guidance/policy/cyber-security-policy-vip-mobile-phones-policy) enabling Ministers and other VIPs to access personal, parliamentary and official business on a single government device
 - Government Security Group [“Corporate by Default” Device Deployment Policy](https://www.security.gov.uk/policy-and-guidance/policy/cyber-security-policy-corporate-by-default-device-deployment-policy/) on which device deployment model to apply to which users
 - [Government Security Classifications Policy](https://www.gov.uk/government/publications/government-security-classifications) and associated guidance on the required security controls and baseline behaviours for the OFFICIAL tier
 - Other applicable cross-government policies published on [this site](https://www.security.gov.uk/policy-and-guidance/policy/) and on GOV.UK
 - Guidance for organisations from the [National Cyber Security Centre (NCSC)](https://www.ncsc.gov.uk/collection/device-security-guidance/bring-your-own-device) on how to securely deploy a BYOD model
 - Guidance for organisations from the [Information Commissioner’s Office](https://ico.org.uk/for-organisations/) on how to uphold information rights in the public interest



## Cyber Assessment Framework outcomes

9.1 The controls described in this policy will help government organisations demonstrate that they have met the required security outcomes in the [NCSC Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/cyber-assessment-framework/introduction-to-caf) (CAF), including but not limited to:

 - A2.a Risk Management Process
 - A3.a Asset Management
 - B2.a Identity Verification, Authentication and Authorisation
 - B2.b Device Management
 - B2.d Identity and Access Management
 - B3.a Understanding Data
 - B3.b Data in Transit
 - B3.d Mobile Data
 - B4.b Secure Configuration
 - B4.c Secure Management
 - C1.a Monitoring Coverage

9.2 The mandatory elements of this policy are aligned with or exceed the [Baseline Government CAF profile](https://www.security.gov.uk/guidance/govassure/government-caf-profiles). Those that exceed the requirements of the profile do so because they are essential to achieving the policy’s core aims.

9.3 For further guidance for government organisations, see [required security outcomes of the CAF](https://www.security.gov.uk/policy/gcsph/).