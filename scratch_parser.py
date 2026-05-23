import json
import re

text = """**1.** Marketing Management mainly involves ____.
a) Only selling products
b) Planning, organizing, directing and controlling marketing activities
c) Managing only finance and production
d) Delivering services without promotion
**Answer: b)**
Marketing management is not just selling — it covers all activities like planning what to sell, organizing teams, directing efforts, and controlling results.

---

**2.** The main aim of marketing management is to ____.
a) Increase costs
b) Satisfy customer needs and achieve business goals
c) Produce as much as possible without demand
d) Focus only on pricing
**Answer: b)**
The whole point of marketing management is to understand what customers want and fulfill those needs while also achieving the company's goals.

---

**3.** Who defined marketing management as the process of planning and executing the conception, pricing, promotion and distribution of ideas, goods and services?
a) Peter Drucker
b) Philip Kotler
c) Henry Fayol
d) F.W. Taylor
**Answer: b)**
Philip Kotler is known as the "Father of Marketing" and gave this famous definition covering all aspects of marketing.

---

**4.** According to Stanton, marketing management involves ____.
a) Only advertising and sales
b) Planning, organizing, directing and controlling exchange activities
c) Financial decision-making
d) Human resource management
**Answer: b)**
Stanton defined marketing management as managing all exchange activities — buying and selling — through planning, organizing, directing, and controlling.

---

**5.** Marketing management connects the company with ____.
a) The government
b) The suppliers
c) The customers
d) The employees only
**Answer: c)**
Marketing management acts as the bridge between the company and its customers by understanding and fulfilling their needs.

---

**6.** Marketing management focuses on building ____.
a) Machinery
b) Strong customer relationships
c) Employee unions
d) Government ties
**Answer: b)**
The core focus of marketing management is building long-term, strong relationships with customers so they keep coming back.

---

**7.** In simple terms, marketing management means ____.
a) Managing only advertisements
b) Managing all marketing activities for business success
c) Controlling employee attendance
d) Creating only product designs
**Answer: b)**
Simply put, marketing management means handling everything related to marketing — from research to promotion — to make the business successful.

---

**8.** The heart of business success, according to marketing management, is ____.
a) Production
b) Marketing
c) Finance
d) Accounting
**Answer: b)**
Marketing is the heart because without it, even the best product won't reach customers. It drives sales and business growth.

---

**9.** The first step in effective marketing management is ____.
a) Pricing the product
b) Identifying customer needs
c) Advertising
d) Recruiting employees
**Answer: b)**
Before doing anything else, a company must first understand what customers actually need. Everything else follows from that.

---

**10.** Marketing management helps in creating demand through ____.
a) Promotions and advertising
b) Cost cutting
c) Employee training
d) Product maintenance
**Answer: a)**
Promotions and advertising inform customers about products and create interest, which leads to demand.

---

**11.** Marketing management encourages companies to develop ____.
a) Outdated products
b) New and innovative products
c) Only cheap products
d) Products with no packaging
**Answer: b)**
To stay competitive and meet changing customer needs, marketing management pushes companies to innovate and develop new products.

---

**12.** Efficient distribution in marketing ensures products reach ____.
a) Suppliers on time
b) Customers at the right place and right time
c) Government agencies
d) Competitors
**Answer: b)**
Distribution is about making sure the product is available where and when the customer wants it — right place, right time.

---

**13.** Customer satisfaction and loyalty are achieved by ____.
a) Ignoring customer feedback
b) Overcharging customers
c) Providing value and good relationships
d) Avoiding service after sales
**Answer: c)**
When a company gives customers good value for money and maintains a good relationship, customers are happy and stay loyal.

---

**14.** Marketing helps in facing competition by ____.
a) Copying competitors' products
b) Studying the market and developing better strategies
c) Ignoring customer needs
d) Reducing product quality
**Answer: b)**
By studying the market and competitors, a company can create smarter strategies to stand out and beat the competition.

---

**15.** Which of the following is a contribution of marketing to the economy?
a) Job creation and trade growth
b) Reduction in innovation
c) Lower employment
d) Limiting product variety
**Answer: a)**
Marketing creates jobs (salespeople, advertisers, etc.) and boosts trade, which helps the overall economy grow.

---

**16.** Marketing management helps in efficient use of resources by ____.
a) Focusing only on profitable markets
b) Ignoring consumer feedback
c) Using manpower randomly
d) Producing more than required
**Answer: a)**
By targeting only profitable and relevant markets, resources like money, time, and manpower are not wasted.

---

**17.** Brand image building through marketing means ____.
a) Creating a negative reputation
b) Building a positive public perception
c) Focusing only on pricing
d) Avoiding advertisements
**Answer: b)**
Marketing helps companies create a good image in the minds of customers, making them trust and prefer that brand.

---

**18.** The 7 Ps model was expanded from the original ____.
a) 3 Ps
b) 4 Ps
c) 5 Ps
d) 6 Ps
**Answer: b)**
The original marketing mix had 4 Ps (Product, Price, Place, Promotion). Three more were added later to make it 7 Ps.

---

**19.** Which of the following is NOT part of the 7 Ps of marketing?
a) Product
b) People
c) Promotion
d) Partnership
**Answer: d)**
The 7 Ps are: Product, Price, Place, Promotion, People, Process, Physical Evidence. "Partnership" is not one of them.

---

**20.** Product in marketing mix refers to ____.
a) Advertising methods
b) Goods or services offered to customers
c) Company profit goals
d) Employee performance
**Answer: b)**
In the 7 Ps, "Product" means what the company is selling — whether it's a physical good or a service.

---

**21.** Price in the 7 Ps represents ____.
a) Company investment
b) Amount customers pay for the product
c) Employee salary
d) Factory cost only
**Answer: b)**
"Price" is what the customer pays to get the product. It must be set carefully to attract customers and still earn profit.

---

**22.** Place in marketing refers to ____.
a) Location where products are stored only
b) Distribution channels used to reach customers
c) Only retail shops
d) Manufacturing plants
**Answer: b)**
"Place" means how the product gets from the company to the customer — through shops, online, agents, etc.

---

**23.** Which element of the 7 Ps involves advertising, sales promotion and public relations?
a) Product
b) Promotion
c) Process
d) People
**Answer: b)**
"Promotion" covers all activities used to communicate and promote the product — ads, discounts, PR campaigns, etc.

---

**24.** People in the marketing mix includes ____.
a) Only customers
b) Employees, sales staff and service providers
c) Only management
d) Suppliers
**Answer: b)**
"People" in the 7 Ps refers to everyone involved in delivering the product/service — staff, salespeople, and service providers.

---

**25.** Physical Evidence in marketing refers to ____.
a) Tangible elements that represent service quality
b) Company budget
c) Human behavior
d) Legal proof
**Answer: a)**
Since services are intangible, "Physical Evidence" means the physical things customers can see/feel — like a clean office, uniform, or brochure — that show quality.

---

**26.** In marketing, needs are defined as ____.
a) Things that people desire for luxury
b) Basic human requirements for survival and well-being
c) Cultural preferences
d) Marketing products sold by companies
**Answer: b)**
Needs are the basic things every human requires — food, shelter, clothing, safety. They exist naturally without marketing.

---

**27.** Which of the following is NOT a basic human need?
a) Food
b) Shelter
c) Respect
d) Television
**Answer: d)**
Food, shelter, and respect are basic needs. A television is a want or luxury, not a basic survival requirement.

---

**28.** Wants are best described as ____.
a) The same for all humans
b) Specific preferences influenced by culture and personality
c) Completely independent of needs
d) Fixed and unchanging
**Answer: b)**
Wants are shaped by culture, society, and personal taste. For example, everyone needs food, but one person may want pizza while another wants rice.

---

**29.** When a person has both desire and ability to pay for a product, it is called ____.
a) Need
b) Want
c) Demand
d) Expectation
**Answer: c)**
Demand = Want + Ability to pay. When someone wants something AND has the money to buy it, it becomes a demand.

---

**30.** According to marketing principles, the starting point of marketing is ____.
a) The product
b) The promotion
c) Understanding customer needs
d) The distribution channel
**Answer: c)**
Marketing always starts by understanding what customers need. Only then can you create the right product and strategy.

---

**31.** A person feels hungry – this is an example of ____.
a) A want
b) A demand
c) A need
d) A product
**Answer: c)**
Hunger is a basic biological need — a requirement for survival that exists naturally.

---

**32.** A customer wanting to buy a pizza instead of home-cooked food shows ____.
a) Need
b) Want
c) Demand
d) Desire
**Answer: b)**
The person needs food (basic need), but specifically choosing pizza is a want — a preference shaped by taste and culture.

---

**33.** When someone orders a Domino's pizza using their salary money, it becomes a ____.
a) Need
b) Want
c) Demand
d) Preference
**Answer: c)**
Now the person has the desire (want) AND the money (ability to pay) — so it becomes demand.

---

**34.** Which statement correctly shows the relationship between the three?
a) Demand → Want → Need
b) Need → Want → Demand
c) Want → Demand → Need
d) Need → Demand → Want
**Answer: b)**
The correct flow is: Need (basic requirement) → Want (specific preference) → Demand (want + buying power).

---

**35.** Marketing begins not with products but with ____.
a) Pricing
b) Advertising
c) Customer needs
d) Profit
**Answer: c)**
Good marketing always starts by identifying what the customer needs, not by making a product first.

---

**36.** A customer saying, "I want a cheap mobile phone," refers to ____.
a) Secret need
b) Stated need
c) Delight need
d) Unstated need
**Answer: b)**
A stated need is what the customer says openly. Here, the customer clearly states they want a cheap phone.

---

**37.** A customer actually requiring a durable, long-lasting mobile phone refers to a ____.
a) Real need
b) Stated need
c) Secret need
d) Hidden want
**Answer: a)**
A real need is what the customer actually needs behind their stated need. They said "cheap" but actually need "durable."

---

**38.** A customer expecting good after-sales service but not mentioning it shows ____.
a) Unstated need
b) Stated need
c) Real need
d) Delight need
**Answer: a)**
An unstated need is something the customer expects but doesn't say out loud — like good service after purchase.

---

**39.** Getting free accessories or surprise gifts with a product represents a ____.
a) Secret need
b) Delight need
c) Real need
d) Stated need
**Answer: b)**
A delight need is something unexpected that pleasantly surprises the customer — like a free gift they didn't ask for.

---

**40.** Buying a premium brand for status or recognition indicates a ____.
a) Secret need
b) Real need
c) Stated need
d) Unstated need
**Answer: a) Secret need**
A secret need is what the customer wants but won't admit openly — like buying a luxury brand just to impress others.

---

**41.** Understanding customer needs is the ___ of marketing.
a) End point
b) Foundation
c) Optional part
d) Final step
**Answer: b)**
Understanding needs is the foundation — the base on which all marketing strategies are built.

---

**42.** Identifying needs and wants helps companies in ____.
a) Guessing demand
b) Developing products that meet real expectations
c) Increasing production only
d) Avoiding product innovation
**Answer: b)**
When companies know what customers truly need, they can make products that actually satisfy them, not just guess.

---

**43.** When marketers understand true customer needs, they can ____.
a) Reduce business risk
b) Increase confusion
c) Waste resources
d) Ignore feedback
**Answer: a)**
Understanding needs means you make the right product for the right audience, which reduces the risk of failure.

---

**44.** Different customer groups with different needs and wants help in ____.
a) Advertising only
b) Market segmentation and targeting
c) Cost control
d) Product packaging
**Answer: b)**
When customers have different needs, the market is divided into segments, and companies target each segment specifically.

---

**45.** A company that meets customer needs better than competitors gains ____.
a) Customer dissatisfaction
b) Competitive advantage
c) Legal risk
d) Market confusion
**Answer: b)**
If your product satisfies customers better than rivals, you gain a competitive advantage — customers prefer you over others.

---

**46.** In the smartphone market, the need is for ____.
a) A particular brand
b) Communication and connectivity
c) Entertainment only
d) Brand recognition
**Answer: b)**
The basic need is to communicate and stay connected. Specific brands or features are wants, not the core need.

---

**47.** The want in the smartphone market example is ____.
a) Owning any phone
b) A smartphone with camera and internet
c) Having no phone
d) Using a landline
**Answer: b)**
The want is a specific version of the need — wanting a smartphone with camera and internet, not just any phone.

---

**48.** The demand in the smartphone example occurs when ____.
a) The customer has no money
b) The customer purchases an iPhone or Samsung
c) The customer just browses online
d) The customer asks for product details
**Answer: b)**
Demand is when the customer actually buys — purchases an iPhone or Samsung — using their money.

---

**49.** The main difference between want and demand is ____.
a) Want has financial support demand does not
b) Demand has willingness and ability to pay want may not
c) Both are same
d) Demand is emotional want is practical
**Answer: b)**
The key difference: Demand = Want + Ability to pay. A want is just a desire; demand is backed by purchasing power.

---

**50.** Marketers study needs, wants and demands primarily to ____.
a) Produce what is easiest
b) Force customers to buy
c) Design products that satisfy real human requirements
d) Focus only on profit
**Answer: c)**
Marketers study these to make products that genuinely fulfill what people need, want, and can afford.

---

**51.** Marketing is mainly concerned with ____.
a) Producing goods only
b) Promoting and selling products or services
c) Accounting and finance
d) Hiring employees
**Answer: b)**
Marketing's main job is to promote products/services and ensure they reach the right customers to generate sales.

---

**52.** The main difference between traditional and digital marketing is ____.
a) Target audience
b) Use of the internet and technology
c) Company size
d) Type of product sold
**Answer: b)**
Traditional marketing uses offline methods; digital marketing uses the internet and technology — that's the core difference.

---

**53.** Both traditional and digital marketing aim to ____.
a) Reduce customer engagement
b) Reach customers and increase sales
c) Eliminate advertising
d) Focus only on local areas
**Answer: b)**
Both types have the same goal — reach as many customers as possible and increase sales, just through different methods.

---

**54.** Traditional marketing refers to ____.
a) Online promotion through websites
b) Offline promotion using print, radio and TV
c) Email and social media marketing
d) Mobile app advertising
**Answer: b)**
Traditional marketing uses offline channels — newspapers, TV, radio, billboards, hoardings — no internet needed.

---

**55.** Which of the following is NOT a traditional marketing method?
a) Television commercials
b) Newspaper ads
c) Search engine optimization
d) Billboards
**Answer: c)**
SEO (Search Engine Optimization) is a digital marketing technique. TV, newspaper ads, and billboards are all traditional.

---

**56.** Direct marketing in traditional methods includes ____.
a) Door-to-door sales and phone calls
b) Social media posts
c) YouTube ads
d) Website pop-ups
**Answer: a)**
Traditional direct marketing means going directly to the customer — door-to-door visits and phone calls, not online methods.

---

**57.** Outdoor advertising includes ____.
a) Brochures
b) TV commercials
c) Billboards and posters
d) Email newsletters
**Answer: c)**
Outdoor advertising is anything placed in public spaces — billboards, hoardings, and posters are classic examples.

---

**58.** Which of the following is an advantage of traditional marketing?
a) High flexibility
b) Builds trust through personal contact
c) Global reach
d) Real-time feedback
**Answer: b)**
Traditional marketing, especially face-to-face selling and print ads, builds trust through personal interaction — something digital can't always replicate.

---

**59.** One major limitation of traditional marketing is that ____.
a) It is cheap and fast
b) It is difficult to measure results
c) It is mostly online
d) It requires no manpower
**Answer: b)**
With a newspaper ad or TV commercial, you can't easily track exactly how many people responded or bought — measurement is hard.

---

**60.** Traditional marketing is most suitable for ____.
a) Businesses targeting a local audience
b) Online-only companies
c) Global e-commerce firms
d) Virtual reality advertising
**Answer: a)**
Traditional methods like local newspapers or radio work best for businesses targeting nearby, local customers.

---

**61.** Digital marketing promotes products through ____.
a) Offline methods
b) The internet and digital platforms
c) Physical stores
d) Newspapers
**Answer: b)**
Digital marketing uses online platforms — websites, social media, apps, email — all powered by the internet.

---

**62.** Which of the following is NOT a method of digital marketing?
a) Search Engine Optimization (SEO)
b) Radio advertising
c) Email marketing
d) Social media marketing
**Answer: b)**
Radio advertising is a traditional method. SEO, email marketing, and social media marketing are all digital.

---

**63.** Social media marketing uses platforms such as ____.
a) Facebook, Instagram and YouTube
b) Newspapers and magazines
c) Radio and TV
d) Door-to-door sales
**Answer: a)**
Social media marketing uses online platforms like Facebook, Instagram, and YouTube to reach and engage customers.

---

**64.** SEO in digital marketing helps to ____.
a) Increase website visibility on search engines
b) Design attractive posters
c) Print advertisements
d) Reduce website traffic
**Answer: a)**
SEO (Search Engine Optimization) makes your website appear higher in Google/Bing search results, bringing more visitors.

---

**65.** Pay-Per-Click (PPC) advertising means ____.
a) Paying employees per task
b) Paying only when users click your advertisement
c) Paying for TV commercials
d) Paying for product packaging
**Answer: b)**
In PPC, you only pay when someone actually clicks on your online ad — making it cost-efficient and measurable.

---

**66.** An advantage of digital marketing is ____.
a) Expensive and time-consuming
b) Hard to measure performance
c) Real-time feedback and analytics
d) No global access
**Answer: c)**
Digital marketing lets you instantly see how your campaign is performing — clicks, views, sales — all in real time.

---

**67.** Which of the following is a limitation of digital marketing?
a) Requires internet access and digital skills
b) Limited customer engagement
c) High printing costs
d) Hard to target specific audiences
**Answer: a)**
Not everyone has internet access or knows how to use digital platforms, which limits digital marketing's reach.

---

**68.** Influencer marketing refers to ____.
a) Hiring famous personalities on social media to promote products
b) Sending flyers to houses
c) Radio promotion
d) Buying billboard space
**Answer: a)**
Influencer marketing uses popular social media personalities (influencers) to promote products to their followers.

---

**69.** Mobile marketing involves ____.
a) Only email campaigns
b) SMS, app notifications and mobile ads
c) Door-to-door campaigns
d) TV sponsorships
**Answer: b)**
Mobile marketing targets customers through their smartphones — via SMS, push notifications, and mobile ads.

---

**70.** Traditional marketing provides mostly ____.
a) One-way communication
b) Two-way interaction
c) Real-time feedback
d) Personalized experience
**Answer: a)**
Traditional marketing (TV, newspaper) broadcasts a message to the audience — no immediate reply or interaction possible.

---

**71.** Digital marketing provides ____.
a) One-way communication
b) Limited reach
c) Two-way communication and engagement
d) Only local advertising
**Answer: c)**
Digital marketing allows customers to like, comment, share, and reply — creating a two-way conversation.

---

**72.** Which of the following has higher flexibility?
a) Traditional marketing
b) Digital marketing
c) Both are equal
d) None
**Answer: b)**
Digital campaigns can be changed instantly — you can edit an online ad in minutes, unlike a printed newspaper ad.

---

**73.** Measuring results and analytics are easier in ____.
a) Traditional marketing
b) Digital marketing
c) Both are same
d) None
**Answer: b)**
Digital marketing tools (Google Analytics, Facebook Insights) give detailed data on performance — traditional can't match this.

---

**74.** In terms of cost, digital marketing is generally ____.
a) More expensive than TV advertising
b) Lower in cost and affordable for small businesses
c) Not measurable
d) Useless for startups
**Answer: b)**
Running a social media or email campaign costs far less than a TV commercial, making it ideal for small businesses.

---

**75.** Which of the following statements is TRUE?
a) Traditional marketing has global reach
b) Digital marketing allows instant feedback
c) Traditional marketing uses social media platforms
d) Digital marketing cannot be measured
**Answer: b)**
Digital marketing allows instant feedback — customers can comment, review, and respond immediately online.

---

**76.** Event Management mainly involves ____.
a) Producing goods for sale
b) Planning, organizing and executing events
c) Managing financial accounts only
d) Hiring employees for companies
**Answer: b)**
Event management is all about planning, organizing, and successfully executing events — from small meetings to big concerts.

---

**77.** The main purpose of event management is to ____.
a) Entertain only the organizers
b) Plan and conduct events efficiently to achieve goals
c) Spend money without planning
d) Focus only on decorations
**Answer: b)**
Events are organized with specific goals — brand promotion, celebration, education — and event management ensures those goals are met efficiently.

---

**78.** Events can be divided based on ____.
a) Season and weather
b) Purpose, audience and scale
c) Price and size
d) Number of participants only
**Answer: b)**
Events are classified by their purpose (corporate, social, etc.), the audience they target, and how large or small they are.

---

**79.** Corporate events are mainly organized by ____.
a) Government departments
b) NGOs
c) Business organizations and companies
d) Individuals for family gatherings
**Answer: c)**
Corporate events like conferences, product launches, and trade shows are organized by businesses for professional purposes.

---

**80.** Which of the following is NOT an example of a corporate event?
a) Conferences
b) Product launches
c) Weddings
d) Trade shows
**Answer: c)**
Weddings are social/personal events. Conferences, product launches, and trade shows are all corporate events.

---

**81.** The main purpose of corporate events is to ____.
a) Celebrate festivals
b) Build brand image and strengthen business relations
c) Promote local art and culture
d) Organize community fairs
**Answer: b)**
Corporate events help companies build their brand reputation and strengthen relationships with clients, partners, and employees.

---

**82.** Social events are related to ____.
a) Professional development
b) Family and personal celebrations
c) Government awareness campaigns
d) Sports competitions
**Answer: b)**
Social events are personal in nature — weddings, birthdays, anniversaries, and other family celebrations.

---

**83.** Which of the following is a social event?
a) Seminar
b) Marathon
c) Wedding
d) Product exhibition
**Answer: c)**
A wedding is a personal/family celebration — a social event. Seminars and marathons fall under other categories.

---

**84.** Cultural events mainly aim to ____.
a) Discuss business strategies
b) Preserve art, music and traditions
c) Conduct examinations
d) Promote health awareness
**Answer: b)**
Cultural events celebrate and preserve a community's art, music, dance, and traditions — like festivals and cultural fests.

---

**85.** Which of the below given is a cultural event?
a) Job fair
b) Dance competition
c) Science exhibition
d) Sports day
**Answer: b)**
A dance competition showcases artistic and cultural expression, making it a cultural event.

---

**86.** Educational events are generally conducted by ____.
a) Schools, colleges and training institutions
b) Hospitals
c) Sports clubs only
d) The army
**Answer: a)**
Educational events like seminars, workshops, and exhibitions are conducted by schools, colleges, and training centers.

---

**87.** The main goal of educational events is ____.
a) Profit generation
b) Fun and recreation
c) Knowledge sharing and skill enhancement
d) Business promotion
**Answer: c)**
The primary purpose of educational events is to share knowledge and help participants learn new skills.

---

**88.** Sports events primarily promote ____.
a) Teamwork and sportsmanship
b) Religious beliefs
c) Political awareness
d) Cultural heritage
**Answer: a)**
Sports events bring people together to compete and build teamwork, discipline, and sportsmanship.

---

**89.** Which of the following is NOT a sports event?
a) Marathon
b) Cricket match
c) DJ night
d) Football tournament
**Answer: c)**
A DJ night is an entertainment event, not a sports event. Marathons, cricket, and football tournaments are all sports.

---

**90.** Entertainment events are organized for ____.
a) Fun, relaxation and enjoyment
b) Education only
c) Employee training
d) Religious teaching
**Answer: a)**
Entertainment events — concerts, award shows, DJ nights — are purely for enjoyment and relaxation.

---

**91.** Which of these is an example of an entertainment event?
a) Film award function
b) Blood donation camp
c) Republic Day parade
d) Science exhibition
**Answer: a)**
A film award function (like Filmfare Awards) is organized for entertainment and celebration of the film industry.

---

**92.** Government and public events are usually organized for ____.
a) Citizens awareness and national pride
b) Private family celebration
c) Product advertising
d) Sports competitions only
**Answer: a)**
Government events like Republic Day, Independence Day, and awareness campaigns are for public benefit and national pride.

---

**93.** Which of the following is a government or public event?
a) Marriage reception
b) Independence Day celebration
c) Music concert
d) Dance festival
**Answer: b)**
Independence Day is a national/public event organized by the government to celebrate the country's freedom.

---

**94.** Religious events mainly focus on ____.
a) Marketing products
b) Spiritual growth and community bonding
c) Political campaigning
d) Product training
**Answer: b)**
Religious events like Ganesh Utsav, Eid, or Christmas gatherings focus on faith, spirituality, and bringing communities together.

---

**95.** Which is an example of a religious event?
a) Ganesh Utsav
b) Business conference
c) Sports day
d) Career fair
**Answer: a)**
Ganesh Utsav is a well-known religious festival celebrated with devotion and community participation.

---

**96.** Fundraising events are organized to ____.
a) Raise funds for social causes
b) Promote luxury brands
c) Entertain celebrities
d) Sell expensive tickets
**Answer: a)**
Fundraising events collect money for charities, NGOs, and social welfare activities — helping people in need.

---

**97.** Which of the following is a fundraising event?
a) Charity dinner
b) Music award show
c) Workshop
d) Science fair
**Answer: a)**
A charity dinner is organized specifically to collect donations for a cause — a classic fundraising event.

---

**98.** The purpose of fundraising and charity events is to ____.
a) Support social welfare and development
b) Increase entertainment value
c) Train government employees
d) Celebrate family milestones
**Answer: a)**
These events exist to raise money and support social causes — like education for the poor, disaster relief, etc.

---

**99.** A college's Annual Day or Cultural Fest is an example of ____.
a) Religious event
b) Corporate event
c) Educational and cultural event
d) Fundraising event
**Answer: c)**
College Annual Days combine education (achievements, awards) and culture (performances, competitions) — making them educational and cultural events.

---

**100.** Which of the following correctly matches the event type with its purpose?
a) Corporate – Entertainment
b) Social – Business growth
c) Religious – Faith and devotion
d) Educational – Family celebration
**Answer: c)**
Religious events are correctly matched with faith and devotion. Corporate events are for business, social for personal celebrations, and educational for learning."""

blocks = re.split(r'\n---\n+', text.strip())
result = []

for block in blocks:
    if not block.strip():
        continue
        
    lines = block.strip().split('\n')
    question_match = re.match(r'\*\*\d+\.\*\*\s+(.*?)$', lines[0])
    if not question_match:
        continue
    
    question = question_match.group(1).strip()
    
    options = []
    i = 1
    while i < len(lines) and not lines[i].startswith('**Answer:'):
        if lines[i].strip():
            options.append(lines[i].strip())
        i += 1
        
    if i >= len(lines):
        continue
        
    answer_match = re.match(r'\*\*Answer:\s+(.*?)\*\*', lines[i])
    if answer_match:
        answer_key = answer_match.group(1).strip()
    else:
        answer_key = ""
        
    # Reconstruct the full answer line based on the key
    answer = ""
    for opt in options:
        if opt.startswith(answer_key):
            answer = opt
            break
            
    # Sometimes it's "**Answer: a) Secret need**"
    if not answer and answer_match:
        answer = answer_match.group(1).strip()
    
    i += 1
    explanation = ""
    while i < len(lines):
        if lines[i].strip():
            explanation += lines[i].strip() + " "
        i += 1
        
    result.append({
        "id": len(result) + 1,
        "question": question,
        "options": options,
        "answer": answer.strip(),
        "explanation": explanation.strip()
    })

with open("e:/Web Development/Projects/ETI mcq/src/data/management_unit4.json", "w", encoding='utf-8') as f:
    json.dump(result, f, indent=4, ensure_ascii=False)

print(f"Parsed {len(result)} questions successfully!")
