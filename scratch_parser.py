import json
import re

text = """**1. The main purpose of a Quality Circle is to ____**
a) Solve workplace problems through teamwork
b) Conduct financial audits
c) Replace management
d) Supervise marketing activities

**Correct: a) Solve workplace problems through teamwork**
Explanation: Quality Circles are small groups of employees who meet regularly to identify and solve work-related problems together as a team.

---

**2. Quality Circles operate on the principle of ____.**
a) Hierarchical control
b) Employee participation and empowerment
c) Autocratic leadership
d) None of the above

**Correct: b) Employee participation and empowerment**
Explanation: Quality Circles believe that employees at all levels should be involved in decision-making and given power to improve their work area.

---

**3. The concept of Quality Circles originated in ____.**
a) USA
b) Japan
c) Germany
d) India

**Correct: b) Japan**
Explanation: Quality Circles were developed in Japan in the 1960s as part of their quality improvement movement after World War II.

---

**4. The founder of the Quality Circle concept is ____**
a) Kaoru Ishikawa
b) W. Edwards Deming
c) Joseph Juran
d) F.W. Taylor

**Correct: a) Kaoru Ishikawa**
Explanation: Kaoru Ishikawa, a Japanese professor, is credited with developing the Quality Circle concept in Japan in the early 1960s.

---

**5. A typical Quality Circle includes ____**
a) 5-10 members from the same department
b) Only managers
c) Outsiders and consultants
d) Directors and shareholders

**Correct: a) 5-10 members from the same department**
Explanation: A Quality Circle is a small group of 5 to 10 workers from the same work area who voluntarily meet to solve problems related to their work.

---

**6. Quality Circles aim at ____**
a) Developing creativity and problem-solving skills
b) Punishing poor performers
c) Cutting salaries
d) Reducing communication

**Correct: a) Developing creativity and problem-solving skills**
Explanation: Quality Circles encourage employees to think creatively, identify problems, and come up with practical solutions, which improves their skills.

---

**7. The main outcome of a Quality Circle meeting is ____**
a) New rules
b) Suggestions for improvement
c) Promotions
d) Financial reports

**Correct: b) Suggestions for improvement**
Explanation: The primary output of Quality Circle meetings is practical suggestions and solutions that can improve quality, productivity, and the work environment.

---

**8. Which of these is often used in Quality Circles?**
a) Fishbone diagram
b) Balance sheet
c) SWOT matrix only
d) Ledger book

**Correct: a) Fishbone diagram**
Explanation: The Fishbone (Cause and Effect) diagram is a common tool used in Quality Circles to identify the root causes of a problem in a visual way.

---

**9. Quality Circle members enhance ____**
a) Motivation and teamwork
b) Isolation among workers
c) Political influence
d) Financial accounting

**Correct: a) Motivation and teamwork**
Explanation: Working in Quality Circles makes employees feel valued and involved, which boosts their motivation and strengthens teamwork.

---

**10. Quality Circles were first introduced in India at ____**
a) BHEL
b) Tata Steel
c) Indian Railways
d) Hindustan Motors

**Correct: a) BHEL**
Explanation: BHEL (Bharat Heavy Electricals Limited) was the first organization in India to introduce Quality Circles in the early 1980s.

---

**11. The ultimate benefit of Quality Circles is ____**
a) Improved quality and productivity
b) Higher bureaucracy
c) Increased absenteeism
d) Less employee involvement

**Correct: a) Improved quality and productivity**
Explanation: When employees regularly identify and solve problems together, it directly leads to better quality products/services and higher productivity.

---

**12. Quality Circles operate on a ____ management approach**
a) Bottom-up
b) Top-down
c) Centralized
d) Bureaucratic

**Correct: a) Bottom-up**
Explanation: In Quality Circles, ideas and improvements come from workers at the ground level (bottom) and go up to management, not the other way around.

---

**13. The term Kaizen means ____**
a) Continuous improvement
b) Sudden innovation
c) Large-scale change
d) Temporary solution

**Correct: a) Continuous improvement**
Explanation: "Kaizen" is a Japanese word where "Kai" means change and "Zen" means good/better. Together it means making continuous small improvements every day.

---

**14. Kaizen is a concept developed in ____**
a) China
b) Japan
c) USA
d) France

**Correct: b) Japan**
Explanation: Kaizen originated in Japan after World War II and was widely used by Japanese companies like Toyota to improve their manufacturing processes continuously.

---

**15. The philosophy of Kaizen emphasizes ____**
a) Small improvements made regularly
b) Major one-time reforms
c) Only technological upgrades
d) Top management control

**Correct: a) Small improvements made regularly**
Explanation: Kaizen focuses on making many small, incremental improvements on a daily basis rather than waiting for one big change.

---

**16. Which statement is most true about Kaizen?**
a) It depends only on expensive equipment
b) It requires employee involvement at all levels
c) It ignores small changes
d) It is used only in manufacturing

**Correct: b) It requires employee involvement at all levels**
Explanation: Kaizen works best when every employee — from top management to floor workers — participates and contributes improvement ideas regularly.

---

**17. The main goal of Kaizen is to ____**
a) Maintain current standards
b) Achieve continuous betterment
c) Increase cost
d) Focus on individuals only

**Correct: b) Achieve continuous betterment**
Explanation: Kaizen's core goal is to never stop improving. It pushes for constant betterment in processes, quality, safety, and efficiency.

---

**18. Which Japanese management practice is closely related to Kaizen?**
a) Just-in-time (JIT)
b) Benchmarking
c) Outsourcing
d) Downsizing

**Correct: a) Just-in-time (JIT)**
Explanation: Just-in-Time (JIT) and Kaizen are both part of the Toyota Production System. JIT reduces waste by producing only what is needed, which aligns with Kaizen's waste-elimination philosophy.

---

**19. A good example of Kaizen is ____**
a) Re-arranging tools to save motion time
b) Hiring more supervisors
c) Conducting annual party
d) Ignoring small details

**Correct: a) Re-arranging tools to save motion time**
Explanation: Rearranging tools so workers can reach them faster is a classic small improvement that saves time and reduces waste — a perfect example of Kaizen in action.

---

**20. Kaizen primarily depends on ____**
a) Continuous employee suggestions
b) Large investments
c) Expensive consultants
d) High turnover

**Correct: a) Continuous employee suggestions**
Explanation: Kaizen relies on employees regularly sharing small ideas and suggestions for improvement rather than expensive technology or outside experts.

---

**21. Which of the following is NOT a principle of Kaizen?**
a) Involve everyone
b) Think improvement every day
c) Blame employees for mistakes
d) Eliminate waste

**Correct: c) Blame employees for mistakes**
Explanation: Kaizen focuses on improving the process, not blaming people. It encourages a positive, blame-free culture where mistakes are seen as opportunities to improve.

---

**22. The PDCA cycle (Plan-Do-Check-Act) is often associated with ____**
a) Kaizen
b) TQM
c) Six Sigma
d) QFD, A and B

**Correct: d) QFD, A and B**
Explanation: The PDCA cycle is used in both Kaizen and TQM. It is a key tool for continuous improvement — plan a change, do it, check the results, and act to standardize it.

---

**23. Six Sigma aims to ____**
a) Reduce defects and variation
b) Increase wastage
c) Limit employee participation
d) Focus on hiring

**Correct: a) Reduce defects and variation**
Explanation: Six Sigma is a data-driven methodology that focuses on identifying and eliminating defects and reducing variation in any process to improve quality.

---

**24. Six Sigma was developed by ____.**
a) Motorola
b) Toyota
c) General Electric
d) Ford

**Correct: a) Motorola**
Explanation: Six Sigma was developed by Motorola engineer Bill Smith in 1986 as a way to improve manufacturing quality and reduce product defects.

---

**25. The statistical goal of Six Sigma is ____.**
a) 3.4 defects per million opportunities
b) 100 defects per million
c) 99% accuracy
d) Zero defects

**Correct: a) 3.4 defects per million opportunities**
Explanation: Six Sigma targets a very high quality level — only 3.4 defects per million opportunities, which means achieving 99.99966% accuracy.

---

**26. The term 'Sigma' represents ____.**
a) Standard deviation
b) Mean value
c) Frequency
d) Total quality

**Correct: a) Standard deviation**
Explanation: Sigma (σ) is a statistical term representing standard deviation, which measures how much variation or spread exists in a process. Higher sigma = less variation = better quality.

---

**27. The DMAIC cycle stands for ____.**
a) Define, Measure, Analyze, Improve, Control
b) Design, Manage, Apply, Implement, Control
c) Direct, Motivate, Assess, Improve, Conclude
d) Define, Monitor, Act, Integrate, Conclude

**Correct: a) Define, Measure, Analyze, Improve, Control**
Explanation: DMAIC is the core problem-solving framework of Six Sigma. Each step helps systematically find the root cause of defects and make lasting improvements.

---

**28. Six Sigma focuses on ____.**
a) Data-driven decision-making
b) Guesswork
c) Top-level authority only
d) Financial auditing

**Correct: a) Data-driven decision-making**
Explanation: Six Sigma uses statistical tools and data analysis to make decisions, not opinions or guesses. Every improvement is backed by measurable evidence.

---

**29. In Six Sigma, Green Belts are ____.**
a) Employees trained to support improvement projects
b) Senior executives
c) Accountants
d) Temporary workers

**Correct: a) Employees trained to support improvement projects**
Explanation: Green Belts are employees trained in Six Sigma methods who work part-time on improvement projects while continuing their regular jobs.

---

**30. Black Belts in Six Sigma are ____.**
a) Team leaders and experts who mentor others
b) New interns
c) Managers of HR department
d) Outsiders

**Correct: a) Team leaders and experts who mentor others**
Explanation: Black Belts are full-time Six Sigma experts who lead improvement projects and mentor Green Belts. They have deep knowledge of statistical tools and DMAIC.

---

**31. Master Black Belt refers to ____.**
a) Person who leads Six Sigma program company-wide
b) Marketing executive
c) Junior trainee
d) None of these

**Correct: a) Person who leads Six Sigma program company-wide**
Explanation: Master Black Belts are the highest level Six Sigma experts who train and coach Black Belts and oversee the entire Six Sigma program across the organization.

---

**32. The main focus of Six Sigma is ____.**
a) Customer satisfaction through defect prevention
b) Product advertising
c) Financial reporting
d) Staff reduction

**Correct: a) Customer satisfaction through defect prevention**
Explanation: Six Sigma ultimately aims to satisfy customers by delivering products and services with minimal defects and consistent quality.

---

**33. Six Sigma projects use which key tool?**
a) Statistical analysis
b) Astrology
c) Random guessing
d) Marketing mix

**Correct: a) Statistical analysis**
Explanation: Six Sigma heavily relies on statistical tools like control charts, regression analysis, and hypothesis testing to identify root causes and measure improvements.

---

**34. Which company popularized Six Sigma after Motorola?**
a) General Electric (GE)
b) Toyota
c) Sony
d) Apple

**Correct: a) General Electric (GE)**
Explanation: Jack Welch, CEO of General Electric, adopted Six Sigma in 1995 and made it famous worldwide by achieving billions of dollars in savings using this methodology.

---

**35. In Six Sigma, process capability is measured in terms of ____.**
a) Sigma levels
b) Mean deviation
c) Cost per unit
d) Time only

**Correct: a) Sigma levels**
Explanation: Sigma levels (1σ to 6σ) indicate how capable a process is. A higher sigma level means fewer defects and better process performance.

---

**36. The ultimate goal of Six Sigma is to achieve ____.**
a) 99.99966% accuracy
b) 80% efficiency
c) Average quality
d) Maximum supervision

**Correct: a) 99.99966% accuracy**
Explanation: At Six Sigma level, a process produces only 3.4 defects per million opportunities, which equals 99.99966% accuracy — near perfection.

---

**37. TQM stands for ____.**
a) Total Quality Management
b) Technical Quality Measurement
c) Team Quality Monitoring
d) Total Quantity Management

**Correct: a) Total Quality Management**
Explanation: TQM stands for Total Quality Management — a management approach focused on long-term success through customer satisfaction and continuous improvement involving everyone in the organization.

---

**38. The key objective of TQM is ____.**
a) Continuous improvement and customer satisfaction
b) Cost cutting only
c) Bureaucratic control
d) Quick profit

**Correct: a) Continuous improvement and customer satisfaction**
Explanation: TQM's main purpose is to keep improving all processes and make sure customers are always satisfied with the product or service quality.

---

**39. The foundation of TQM lies in ____.**
a) Quality at every stage
b) Inspection only
c) Blaming workers
d) Reducing production

**Correct: a) Quality at every stage**
Explanation: TQM believes quality should be built into every step of the process — from raw materials to final delivery — not just checked at the end.

---

**40. TQM requires participation of ____.**
a) All employees
b) Only managers
c) Only production staff
d) External consultants

**Correct: a) All employees**
Explanation: TQM is a company-wide approach. Every single employee, from top management to the shop floor, must be committed to quality improvement for TQM to work.

---

**41. The famous 14 points of quality management were proposed by ____.**
a) W. Edwards Deming
b) Joseph Juran
c) Kaoru Ishikawa
d) Philip Crosby

**Correct: a) W. Edwards Deming**
Explanation: W. Edwards Deming proposed his famous 14 Points for Management as a guide for transforming business effectiveness and achieving quality.

---

**42. "Fitness for use" definition of quality was given by ____.**
a) Juran
b) Deming
c) Taylor
d) Crosby

**Correct: a) Juran**
Explanation: Joseph Juran defined quality as "fitness for use," meaning a product or service should meet the needs and expectations of the customer when they use it.

---

**43. The "Zero Defect" concept was given by ____.**
a) Philip Crosby
b) Ishikawa
c) Juran
d) Deming

**Correct: a) Philip Crosby**
Explanation: Philip Crosby introduced the "Zero Defects" concept, arguing that the standard should be to do things right the first time with no defects acceptable.

---

**44. A core principle of TQM is ____.**
a) Doing things right the first time
b) Reacting after errors
c) Blaming others
d) Ignoring feedback

**Correct: a) Doing things right the first time**
Explanation: TQM promotes prevention over correction. The idea is to get quality right from the start rather than fixing mistakes later, which saves time and cost.

---

**45. TQM promotes ____.**
a) Customer-driven organization
b) Profit-driven only
c) Technology-driven only
d) Manager-driven

**Correct: a) Customer-driven organization**
Explanation: In TQM, the customer's needs and satisfaction are the driving force behind every decision and process improvement in the organization.

---

**46. TQM emphasizes the use of ____.**
a) Quality tools like Pareto chart, Histogram, Check Sheet
b) Financial tools
c) Advertising campaigns
d) Sales analysis

**Correct: a) Quality tools like Pareto chart, Histogram, Check Sheet**
Explanation: TQM uses specific quality tools such as Pareto charts (to find major problems), Histograms (to show data distribution), and Check Sheets (to collect data) to analyze and improve processes.

---

**47. Which of the following is NOT an element of TQM?**
a) Continuous improvement
b) Employee participation
c) Customer focus
d) Rigid hierarchy

**Correct: d) Rigid hierarchy**
Explanation: TQM promotes open communication, teamwork, and employee involvement at all levels. A rigid hierarchy goes against TQM principles by blocking participation.

---

**48. The Plan-Do-Check-Act (PDCA) cycle is used in TQM for ____.**
a) Continuous improvement
b) Marketing
c) Recruitment
d) Financial planning

**Correct: a) Continuous improvement**
Explanation: The PDCA cycle is TQM's tool for continuous improvement — Plan what to improve, Do it on a small scale, Check if it worked, and Act to standardize the improvement.

---

**49. Which of the following is a benefit of TQM?**
a) Improved morale and productivity
b) More errors
c) Reduced teamwork
d) Increased supervision

**Correct: a) Improved morale and productivity**
Explanation: When employees are involved in quality improvement and see their ideas implemented, it boosts their morale. Better processes also naturally lead to higher productivity.

---

**50. The ultimate aim of TQM is to achieve ____.**
a) Long-term customer loyalty and organizational excellence
b) Short-term gains
c) Maximum supervision
d) Minimum employee involvement

**Correct: a) Long-term customer loyalty and organizational excellence**
Explanation: TQM is not about quick fixes. Its ultimate goal is to build an organization that consistently delivers excellent quality, earning long-term customer loyalty.

---

**51. The main purpose of 5S is to ____.**
a) Increase sales
b) Organize the workplace and improve efficiency
c) Hire more workers
d) Reduce salaries

**Correct: b) Organize the workplace and improve efficiency**
Explanation: 5S is a workplace organization method that creates a clean, organized, and efficient work environment to reduce waste and improve productivity.

---

**52. 5S originated in which country?**
a) China
b) USA
c) Japan
d) Germany

**Correct: c) Japan**
Explanation: 5S originated in Japan and was developed as part of the Toyota Production System to organize the workplace and eliminate waste.

---

**53. In 5S, 'Seiri' stands for ____.**
a) Set in order
b) Sort - remove unnecessary items
c) Shine
d) Sustain - maintain standards

**Correct: b) Sort - remove unnecessary items**
Explanation: Seiri (Sort) is the first S. It means going through all items in the workplace and removing everything that is not needed for current work.

---

**54. The second 'S', 'Seiton' means ____.**
a) Standardize
b) Set things in order for easy access
c) Shine
d) Sustain improvements

**Correct: b) Set things in order for easy access**
Explanation: Seiton (Set in Order) means arranging all necessary items in a proper place so they can be easily found, used, and returned after use.

---

**55. 'Seiso' refers to ____.**
a) Keeping the workplace neat and clean
b) Sorting out materials
c) Labeling items
d) Conducting audits

**Correct: a) Keeping the workplace neat and clean**
Explanation: Seiso (Shine) means regularly cleaning the workplace. A clean environment helps identify problems like leaks, damage, or misplaced items quickly.

---

**56. The fourth 'S' - 'Seiketsu' means ____.**
a) Shining tools
b) Standardizing procedures
c) Sustaining improvements
d) Sorting and discarding waste

**Correct: b) Standardizing procedures**
Explanation: Seiketsu (Standardize) means creating standard rules and procedures so that the first three S's (Sort, Set, Shine) are done consistently every day.

---

**57. The fifth 'S', 'Shitsuke,' means ____.**
a) Sorting
b) Discipline and sustaining the habit of 5S
c) Supervising workers
d) Scheduling production

**Correct: b) Discipline and sustaining the habit of 5S**
Explanation: Shitsuke (Sustain) means making 5S a habit through self-discipline. It ensures that all the improvements made are maintained long-term without being forced.

---

**58. The main benefit of 5S is ____.**
a) Lower product quality
b) Clean, safe and efficient workplace
c) Increased paperwork
d) Less teamwork

**Correct: b) Clean, safe and efficient workplace**
Explanation: 5S creates a workplace that is clean, well-organized, and safe, which reduces accidents, saves time searching for items, and improves overall efficiency.

---

**59. Which of the following is NOT part of the 5S system?**
a) Seiri
b) Seiso
c) Shitsuke
d) Six Sigma

**Correct: d) Six Sigma**
Explanation: The 5S system consists of Seiri, Seiton, Seiso, Seiketsu, and Shitsuke. Six Sigma is a completely separate quality improvement methodology.

---

**60. The 5S method is most closely related to ____.**
a) Lean manufacturing and continuous improvement
b) Advertising strategy
c) Finance and accounting
d) Marketing management

**Correct: a) Lean manufacturing and continuous improvement**
Explanation: 5S is a foundational tool of Lean Manufacturing. It eliminates waste through workplace organization and supports the continuous improvement culture.

---

**61. A red tag is commonly used during which 5S stage?**
a) Seiketsu
b) Seiri (Sorting)
c) Seiso
d) Shitsuke

**Correct: b) Seiri (Sorting)**
Explanation: During Seiri (Sort), red tags are placed on items that are unnecessary or questionable. These tagged items are then evaluated for removal, relocation, or disposal.

---

**62. The goal of 'Set in Order' is to ____.**
a) Arrange items so they are easy to find and return
b) Store items randomly
c) Remove all tools from the area
d) Paint the walls

**Correct: a) Arrange items so they are easy to find and return**
Explanation: Set in Order (Seiton) means every item has a fixed place. This saves time, reduces frustration, and ensures tools are always available when needed.

---

**63. Regular cleaning, inspection and maintenance belong to which S?**
a) Seiso (Shine)
b) Seiketsu (Standardize)
c) Shitsuke (Sustain)
d) Seiri (Sort)

**Correct: a) Seiso (Shine)**
Explanation: Seiso (Shine) involves not just cleaning but also inspecting equipment during cleaning to detect any abnormalities or problems early.

---

**64. 5S helps to eliminate which of the following wastes?**
a) Overproduction
b) Unnecessary motion and time waste
c) Marketing costs
d) None of these

**Correct: b) Unnecessary motion and time waste**
Explanation: By organizing the workplace properly, 5S eliminates time wasted searching for tools, unnecessary movements, and delays due to clutter.

---

**65. The ultimate goal of 5S is to ____.**
a) Create a culture of discipline and continuous improvement
b) Reduce prices
c) Maintain paperwork
d) Focus only on profits

**Correct: a) Create a culture of discipline and continuous improvement**
Explanation: Beyond just cleaning, the ultimate purpose of 5S is to build a disciplined workplace culture where employees continuously improve their work environment.

---

**66. The word 'Kanban' is derived from which language?**
a) English
b) Japanese
c) Chinese
d) Korean

**Correct: b) Japanese**
Explanation: Kanban is a Japanese word. "Kan" means visual and "Ban" means card or board, so Kanban literally means "visual card" or "signboard."

---

**67. The meaning of 'kanban' is ____.**
a) Visual signal or card
b) Machine maintenance
c) Work scheduling software
d) Raw material storage

**Correct: a) Visual signal or card**
Explanation: Kanban means a visual signal (usually a card) used to trigger an action — like replenishing a part or starting production of an item.

---

**68. The Kanban system was first developed by ____.**
a) Motorola
b) Toyota Motor Corporation
c) Ford Motor Company
d) General Electric

**Correct: b) Toyota Motor Corporation**
Explanation: Taiichi Ohno at Toyota developed the Kanban system in the late 1940s inspired by supermarket restocking methods, as part of the Toyota Production System.

---

**69. Kanban is mainly used in which production system?**
a) Just-in-Time (JIT)
b) Mass production
c) Batch production
d) Project-based production

**Correct: a) Just-in-Time (JIT)**
Explanation: Kanban is the signaling tool used in JIT production. It ensures materials and products are made and delivered exactly when needed — not before, not after.

---

**70. The main purpose of a Kanban system is to _____**
a) Increase inventory levels
b) Control production and material flow visually
c) Increase paperwork
d) Delay production

**Correct: b) Control production and material flow visually**
Explanation: Kanban uses visual cards/signals to control how materials move through the production process, preventing overproduction and reducing inventory.

---

**71. In the Kanban method, each card represents _____**
a) A maintenance report
b) A production order or part requirement
c) A customer complaint
d) A financial record

**Correct: b) A production order or part requirement**
Explanation: Each Kanban card acts as an authorization signal — it tells the previous workstation to produce more or supply more of a specific item.

---

**72. Kanban helps in achieving which of the following?**
a) Overproduction
b) Continuous flow and reduced waste
c) Maximum storage
d) Increased downtime

**Correct: b) Continuous flow and reduced waste**
Explanation: By producing only what is needed when it is needed, Kanban creates a smooth continuous flow of production and eliminates waste from overproduction and excess inventory.

---

**73. Which of the following best describes the Kanban principle?**
a) Push system of production
b) Pull system of production
c) Mixed system
d) Random system

**Correct: b) Pull system of production**
Explanation: Kanban is a pull system — production is triggered by actual customer demand or consumption. Work starts only when the next step "pulls" for it, not in advance.

---

**74. In a pull-based Kanban system _____.**
a) Work is started only when there is demand from the next process
b) Production continues regardless of demand
c) Raw materials are ordered in bulk
d) Workers guess production levels

**Correct: a) Work is started only when there is demand from the next process**
Explanation: In a pull system, each stage of production only produces what the next stage actually needs. This avoids building up unnecessary stock or work-in-progress.

---

**75. The two-card Kanban system consists of _____.**
a) Transport Kanban and Production Kanban
b) Delivery Kanban and Finance Kanban
c) Planning Kanban and Cost Kanban
d) Service Kanban and Product Kanban

**Correct: a) Transport Kanban and Production Kanban**
Explanation: The two-card system uses a Production Kanban (to authorize making parts) and a Transport/Withdrawal Kanban (to authorize moving parts to the next process).

---

**76. Kanban is mainly used to _____**
a) Signal the need to move materials or produce parts
b) Replace supervisors
c) Increase inspection frequency
d) Eliminate teamwork

**Correct: a) Signal the need to move materials or produce parts**
Explanation: The main function of Kanban is to act as a visual signal that tells workers when to produce more or when to move materials from one process to another.

---

**77. Which of the following is NOT an advantage of Kanban?**
a) Reduces inventory
b) Improves workflow
c) Increases complexity
d) Visualizes the production process

**Correct: c) Increases complexity**
Explanation: Kanban actually simplifies the production process. Reducing inventory, improving workflow, and visual management are all advantages. Increasing complexity is not.

---

**78. Kanban cards can be replaced by which of the following modern equivalents?**
a) Electronic signals, barcodes, or RFID tags
b) Manual logs
c) Paper forms
d) Phone calls

**Correct: a) Electronic signals, barcodes, or RFID tags**
Explanation: In modern digital factories, physical Kanban cards have been replaced by electronic systems like barcodes, RFID tags, and digital dashboards that serve the same signaling purpose.

---

**79. The Kanban system supports which key Lean concept?**
a) Just-in-Time (JIT)
b) Six Sigma
c) Total Quality Management (TQM)
d) Batch production

**Correct: a) Just-in-Time (JIT)**
Explanation: Kanban is the practical tool that makes JIT possible. It ensures materials and production happen exactly when needed, which is the core idea of JIT.

---

**80. The goal of Kanban in production is to ____**
a) Produce only what is needed, when it is needed
b) Produce maximum quantity regardless of demand
c) Stop production frequently
d) Store large quantities of finished goods

**Correct: a) Produce only what is needed, when it is needed**
Explanation: This is the fundamental goal of Kanban — eliminate overproduction by making sure each item is produced only when there is an actual need for it.

---

**81. Which of the following is a type of Total Maintenance?**
a) Total Planned Maintenance
b) Total Productive Maintenance
c) Total Product Management
d) Total Preventive Management

**Correct: b) Total Productive Maintenance**
Explanation: TPM stands for Total Productive Maintenance. It is a system that involves all employees in maintaining equipment to maximize productivity and minimize breakdowns.

---

**82. The main objective of TPM is to ____**
a) Increase machine breakdowns
b) Maximize equipment efficiency and eliminate waste
c) Decrease supervision
d) Reduce operator involvement

**Correct: b) Maximize equipment efficiency and eliminate waste**
Explanation: TPM aims to achieve maximum equipment effectiveness by involving operators in daily maintenance, preventing breakdowns before they happen.

---

**83. JIT (Just-in-time) is a _____ philosophy**
a) Waste driven
b) Demand driven
c) Process driven
d) Profit driven

**Correct: b) Demand driven**
Explanation: JIT produces and delivers goods based on actual customer demand. Nothing is made in advance or stored as excess inventory — production is triggered only by demand.

---

**84. Kanban is a**
a) Visual tool
b) Bar graph
c) Pie chart
d) Process chart

**Correct: a) Visual tool**
Explanation: Kanban is fundamentally a visual management tool. It uses cards, boards, or signals that can be seen by everyone to communicate the status and flow of work.

---

**85. Poka yoke is a**
a) Mistake proofing technique
b) Japanese concept
c) Process improvement technique
d) Quality improvement tool

**Correct: a) Mistake proofing technique**
Explanation: Poka-Yoke is a Japanese term meaning "mistake proofing." It involves designing processes or devices in a way that prevents errors from happening or makes them immediately obvious.

---

**86. The five pillars of 5S are**
a) Sort, Set in order, Shine, Standardize, Sustain
b) Safety, Security, Sanitation, Scheduling, Sales
c) Sort, Store, Ship, Sell, Save
d) Speed, Service, Safety, Satisfaction, Success

**Correct: a) Sort, Set in order, Shine, Standardize, Sustain**
Explanation: The 5S pillars are: Sort (Seiri), Set in Order (Seiton), Shine (Seiso), Standardize (Seiketsu), and Sustain (Shitsuke) — five steps to organize and maintain a productive workplace.

---

**87. Gemba refers to**
a) The actual place where work happens
b) A type of Japanese management philosophy
c) A quality control technique
d) A production system

**Correct: a) The actual place where work happens**
Explanation: Gemba is a Japanese term meaning "the real place" — it refers to the actual workplace (factory floor, shop, site) where value is created and problems should be observed directly.

---

**88. SMED stands for**
a) Single Minute Exchange of Die
b) System for Managing Equipment and Dies
c) Standard Method for Equipment Development
d) Structured Manufacturing Efficiency Development

**Correct: a) Single Minute Exchange of Die**
Explanation: SMED is a Lean manufacturing technique that aims to reduce machine changeover/setup time to under 10 minutes (single-digit minutes), improving flexibility and reducing downtime.

---

**89. TPM emphasizes which type of maintenance?**
a) Breakdown maintenance
b) Preventive and Autonomous maintenance
c) Emergency maintenance
d) Extensive maintenance only

**Correct: b) Preventive and Autonomous maintenance**
Explanation: TPM stresses Preventive Maintenance (scheduled maintenance to prevent failures) and Autonomous Maintenance (operators maintain their own machines daily).

---

**90. The TPM concept includes how many major pillars?**
a) 3
b) 5
c) 8
d) 10

**Correct: c) 8**
Explanation: TPM is built on 8 pillars: Autonomous Maintenance, Focused Improvement, Planned Maintenance, Quality Maintenance, Early Equipment Management, Education and Training, Safety & Environment, and TPM in Administration.

---

**91. Which of the following is NOT one of the 8 Pillars of TPM?**
a) Autonomous Maintenance
b) Focused Improvement
c) Product Design
d) Education and Training

**Correct: c) Product Design**
Explanation: Product Design is not one of the 8 TPM pillars. The 8 pillars focus on maintenance, improvement, safety, training, and equipment management — not product design.

---

**92. The first pillar of TPM, 'Autonomous Maintenance', means ____.**
a) Operators clean, inspect and maintain their own machines
b) Only maintenance staff clean machines
c) Maintenance is ignored
d) Outsiders repair machines

**Correct: a) Operators clean, inspect and maintain their own machines**
Explanation: Autonomous Maintenance empowers machine operators to take ownership of their equipment by performing daily cleaning, inspection, and basic maintenance themselves.

---

**93. Which of the following is a key benefit of TPM?**
a) Reduced downtime and improved productivity
b) Increased waste
c) Higher defect rate
d) More accidents

**Correct: a) Reduced downtime and improved productivity**
Explanation: TPM prevents unexpected machine breakdowns through regular maintenance, which reduces downtime, improves equipment reliability, and boosts overall productivity.

---

**94. The formula for Overall Equipment Effectiveness (OEE) involves**
a) Availability × Performance × Quality
b) Quantity × Time × Speed
c) Cost × Profit × Revenue
d) Safety × Speed × Staff

**Correct: a) Availability × Performance × Quality**
Explanation: OEE measures how effectively equipment is used. Availability (is machine running?), Performance (is it running at full speed?), and Quality (is it producing good parts?) are multiplied together.

---

**95. TPM aims to create a work culture of ____.**
a) Reactive actions
b) Proactive participation and ownership by all employees
c) Blaming maintenance staff
d) Minimal operator training

**Correct: b) Proactive participation and ownership by all employees**
Explanation: TPM shifts the culture from reacting to breakdowns to proactively preventing them. Every employee takes ownership of equipment care rather than waiting for problems to occur.

---

**96. The main objective of Lean Manufacturing is to ____.**
a) Reduce workforce
b) Eliminate waste and improve value to the customer
c) Increase paperwork
d) Expand bureaucracy

**Correct: b) Eliminate waste and improve value to the customer**
Explanation: Lean Manufacturing focuses on delivering maximum value to the customer while using minimum resources by identifying and eliminating all forms of waste in the production process.

---

**97. Lean Manufacturing originated from which company?**
a) Ford Motors
b) Toyota Motor Corporation
c) General Electric
d) Motorola

**Correct: b) Toyota Motor Corporation**
Explanation: Lean Manufacturing evolved from the Toyota Production System (TPS) developed by Taiichi Ohno and Eiji Toyoda at Toyota in post-war Japan.

---

**98. The Toyota Production System (TPS) is the foundation of ____**
a) Total Quality Management
b) Lean Manufacturing
c) Six Sigma
d) Kaizen only

**Correct: b) Lean Manufacturing**
Explanation: Lean Manufacturing is based on the principles and practices of the Toyota Production System (TPS), which pioneered the concepts of waste elimination and continuous flow.

---

**99. The Japanese term 'Muda' refers to ____.**
a) Improvement
b) Waste or non-value-added activity
c) Speed
d) Quality control

**Correct: b) Waste or non-value-added activity**
Explanation: Muda means waste in Japanese — any activity that consumes resources (time, materials, money) without adding value to the customer. Lean aims to eliminate all Muda.

---

**100. How many types of waste (Muda) are identified in Lean?**
a) 3
b) 5
c) 7
d) 9

**Correct: c) 7**
Explanation: Lean identifies 7 types of waste (Muda): Overproduction, Waiting, Transportation, Over-processing, Inventory, Motion, and Defects — remembered by the acronym TIMWOOD or DOWNTIME.

---

**101. Which of the following is NOT one of the seven wastes in Lean?**
a) Overproduction
b) Waiting time
c) Product design
d) Defects

**Correct: c) Product design**
Explanation: Product design is not one of the 7 wastes. The seven wastes are Overproduction, Waiting, Transportation, Over-processing, Inventory, Motion, and Defects.

---

**102. The Lean principle that focuses on 'producing only what is needed when it is needed' is known as ____**
a) JIT (Just-In-Time)
b) TQM
c) MRP
d) ERP

**Correct: a) JIT (Just-In-Time)**
Explanation: Just-In-Time (JIT) is the Lean principle of producing the right product, in the right quantity, at the right time — eliminating overproduction and excess inventory."""

blocks = re.split(r'\n---\n+', text.strip())
result = []

for block in blocks:
    if not block.strip():
        continue
        
    lines = block.strip().split('\n')
    question_match = re.match(r'\*\*\d+\.\s+(.*?)\*\*', lines[0])
    if not question_match:
        continue
    
    question = question_match.group(1).strip()
    
    options = []
    i = 1
    while i < len(lines) and not lines[i].startswith('**Correct:'):
        if lines[i].strip():
            options.append(lines[i].strip())
        i += 1
        
    if i >= len(lines):
        continue
        
    answer_match = re.match(r'\*\*Correct:\s+(.*?)\*\*', lines[i])
    answer = answer_match.group(1).strip() if answer_match else ""
    
    i += 1
    explanation = ""
    if i < len(lines) and lines[i].startswith('Explanation:'):
        explanation = lines[i].replace('Explanation:', '').strip()
        
    result.append({
        "id": len(result) + 1,
        "question": question,
        "options": options,
        "answer": answer,
        "explanation": explanation
    })

with open("e:/Web Development/Projects/ETI mcq/src/data/management_unit3.json", "w", encoding='utf-8') as f:
    json.dump(result, f, indent=4, ensure_ascii=False)

print(f"Parsed {len(result)} questions successfully!")
