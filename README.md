# AdGenius AI: منصة تسويق وإعلانات بالذكاء الاصطناعي

## المرحلة 1: تحليل المتطلبات وتصميم Architecture

### 1.1. ملخص المشروع

AdGenius AI هي منصة ذكاء اصطناعي متكاملة تعمل كفريق تسويق وإعلانات للشركات والأفراد. تهدف المنصة إلى أتمتة مهام التسويق والإعلان من خلال نظام Multi-Agent متطور، يقدم حلولاً شاملة بدءًا من تحليل السوق وحتى تحليل أداء الحملات.

### 1.2. المتطلبات الرئيسية

*   **نظام Multi-Agent:** يتكون من 5 وكلاء متخصصين (Marketing Research, Copywriting, Creative, Campaign Strategy, Analytics).
*   **وظائف MVP:**
    *   **المدخلات:** اسم المنتج، وصف المنتج، السعر، الجمهور المستهدف.
    *   **المخرجات:** خطة إعلان كاملة، نصوص إعلانية، أفكار تصاميم، أفكار فيديو، استراتيجية تسويق.
*   **التقنيات:**
    *   **Backend:** Python + FastAPI
    *   **Frontend:** React + Tailwind CSS
    *   **Database:** PostgreSQL
    *   **Architecture:** Modular + Scalable
    *   **AI:** دعم النماذج مفتوحة المصدر (Qwen, DeepSeek, Llama).
*   **قواعد مهمة:** تصميم هندسي أولاً، شرح القرارات التقنية، هيكل ملفات احترافي، كود قابل للتطوير، لا خدمات مدفوعة في MVP، جاهزية للتحول إلى SaaS عالمي.

### 1.3. تحليل المصادر المفتوحة

تم تحليل أربعة مشاريع مفتوحة المصدر للاستفادة من أفكارها وتصاميمها:

#### 1.3.1. Alibaba Agentic-ADK [1]

*   **الوصف:** إطار عمل لتطوير تطبيقات الوكلاء (Agent applications) من Alibaba International AI Business، مبني على Google-ADK و Ali-LangEngine.
*   **الاستفادة:**
    *   **هندسة الوكلاء:** يوفر مفاهيم قوية لتطوير الوكلاء (LlmAgent, SequentialAgent, LoopAgent, ParallelAgent, CustomAgents, Multi-Agent Systems) وأدوات (Function Tool, AgentTool). هذا سيوجهنا في تصميم وكلاء AdGenius AI.
    *   **المرونة والتوسع:** يدعم أنماط تنفيذ متعددة (متزامن، غير متزامن، تدفق، متوازي) وبروتوكول A2A (Agent-to-Agent)، وهو أمر حيوي لنظام Multi-Agent قابل للتوسع.
    *   **دعم LLM:** يتوافق مع نماذج لغوية كبيرة متنوعة مثل Qwen، مما يتوافق مع متطلباتنا لدعم النماذج مفتوحة المصدر.
    *   **إدارة السياق والذاكرة:** يوفر آليات لتوسيع سياق محادثات الوكلاء (Session, Memory, Artifact)، وهو أمر بالغ الأهمية للحفاظ على استمرارية المعلومات بين الوكلاء.
    *   **التصحيح والتقييم:** ميزات التصحيح والتقييم الجاهزة ستكون مفيدة في تطوير واختبار الوكلاء.

#### 1.3.2. Spring AI Alibaba [2]

*   **الوصف:** إطار عمل للذكاء الاصطناعي مبني على Spring AI لمطوري Java، يوفر تجريدًا عالي المستوى لواجهة برمجة تطبيقات الذكاء الاصطناعي وتكامل البنية التحتية السحابية.
*   **الاستفادة:**
    *   **أتمتة سير العمل:** على الرغم من أنه مبني بلغة Java، إلا أن مفاهيم سير العمل القائمة على الرسم البياني (Graph-based Workflow) والتنسيق بين الوكلاء (Multi-Agent Orchestration) مع أنماط مثل `SequentialAgent` و `ParallelAgent` و `RoutingAgent` ستكون مصدر إلهام لتصميم تدفقات العمل في AdGenius AI.
    *   **هندسة السياق (Context Engineering):** ممارساته المضمنة لتحسين موثوقية وأداء الوكيل من خلال إدارة السياق (Human In The Loop, context compaction, context editing) ستكون مفيدة.
    *   **دعم النماذج والأدوات:** يدعم مزودي LLM المتعددين واستدعاء الأدوات، مما يعزز مرونة نظامنا.

#### 1.3.3. ViGenAiR [3]

*   **الوصف:** مشروع من Google Marketing Solutions لإعادة صياغة إعلانات الفيديو باستخدام الذكاء الاصطناعي التوليدي، يحول إعلانات الفيديو الطويلة إلى صيغ أقصر ومتعددة.
*   **الاستفادة:**
    *   **الوكيل الإبداعي (Creative Agent):** يوفر أفكارًا قوية لتطوير وكيلنا الإبداعي، خاصة في توليد أفكار الفيديو والصور. يمكننا استلهام آليات تقسيم الفيديو، وتحديد الإطارات الرئيسية، وتوليد الأصول النصية للطلب (Demand Gen text assets).
    *   **التعامل مع الوسائط المتعددة:** على الرغم من اعتماده على GCP، فإن نهجه في معالجة الفيديو والصور وتوليدها باستخدام نماذج الذكاء الاصطناعي التوليدي سيوجهنا في تصميم مكونات الوسائط المتعددة في AdGenius AI.
    *   **واجهة المستخدم:** الواجهة الأمامية (Angular UI) يمكن أن توفر إلهامًا لتصميم واجهة المستخدم الخاصة بنا في React.

#### 1.3.4. Adios [4]

*   **الوصف:** حل مفتوح المصدر من Google Marketing Solutions لإدارة أصول صور إعلانات Google، يسهل تحميل الصور وربطها بالحملات الإعلانية.
*   **الاستفادة:**
    *   **إدارة الأصول:** على الرغم من تركيزه على الصور، فإن مفهوم إدارة الأصول (asset management) وربطها بالحملات الإعلانية سيكون ذا صلة بوكيلنا الإبداعي ووكيل استراتيجية الحملة.
    *   **توليد المطالبات (Prompt Generation):** ميزة توليد المطالبات من النص إلى الصورة (Text-to-Image prompt generation) يمكن أن تكون جزءًا أساسيًا من وكيلنا الإبداعي.

### 1.4. تصميم Architecture المقترح لـ AdGenius AI

سنعتمد على بنية **Microservices** لضمان قابلية التوسع والمرونة، مع التركيز على نمط **Event-Driven Architecture** للتواصل بين الوكلاء. سيتم تقسيم النظام إلى المكونات الرئيسية التالية:

#### 1.4.1. المكونات الرئيسية

1.  **Gateway / API Gateway (FastAPI):**
    *   نقطة الدخول الوحيدة لجميع طلبات الواجهة الأمامية (Frontend).
    *   مسؤول عن المصادقة (Authentication) والترخيص (Authorization).
    *   توجيه الطلبات إلى الخدمات الخلفية (Backend Services) المناسبة.
    *   يمكن استخدام FastAPI لإنشاء هذه البوابة بكفاءة.

2.  **Backend Services (FastAPI + Python):**
    *   كل وكيل (Agent) سيكون خدمة FastAPI منفصلة أو مجموعة من الوحدات المنطقية داخل خدمة واحدة كبيرة في MVP، قابلة للفصل لاحقًا.
    *   **Agent Orchestrator Service:** خدمة مركزية لتنسيق تدفق العمل بين الوكلاء. ستتلقى المدخلات من المستخدم وتوجهها إلى الوكيل المناسب، وتجمع المخرجات من الوكلاء المختلفين.
    *   **Agent Services (5 Agents):**
        *   **Marketing Research Agent Service:** يستقبل اسم المنتج، الوصف، الجمهور المستهدف. يستخدم نماذج LLM مفتوحة المصدر (Qwen, DeepSeek, Llama) لتحليل السوق والمنافسين والجمهور، واستخراج نقاط البيع الفريدة (USPs). قد يتضمن أدوات بحث ويب (Web Search Tools) إذا سمحت الميزانية لاحقًا، ولكن في MVP سيعتمد على معلومات LLM الداخلية.
        *   **Copywriting Agent Service:** يستقبل USPs ومعلومات المنتج والجمهور. يستخدم LLM لتوليد نصوص إعلانية احترافية، عناوين، أوصاف، وعبارات تحث المستخدم على اتخاذ إجراء (CTAs). سيعتمد على تقنيات توليد النصوص المتعددة (multiple ad copies generation).
        *   **Creative Agent Service:** يستقبل معلومات المنتج، USPs، والجمهور. يستخدم LLM لتوليد أفكار تصاميم إعلانية، أفكار صور، وسيناريوهات فيديو قصيرة. يمكن أن يعتمد على وصف نصي لإنشاء أفكار بصرية. في MVP، لن يقوم بتوليد الصور/الفيديوهات فعليًا، بل سيقدم الأفكار النصية التي تصفها.
        *   **Campaign Strategy Agent Service:** يستقبل معلومات المنتج، الجمهور، الميزانية المقترحة. يستخدم LLM لبناء خطة حملة إعلانية، اقتراح المنصات المناسبة، وتحديد استراتيجيات استهداف الجمهور.
        *   **Analytics Agent Service:** في MVP، قد يكون هذا الوكيل مبدئيًا عبارة عن محاكاة أو تصميم نظري لكيفية تحليل النتائج واقتراح التحسينات، حيث لا توجد حملات حقيقية لتحليلها بعد. يمكن أن يقدم توصيات عامة بناءً على أفضل الممارسات.
    *   **Shared Utilities/Libraries:** مكتبات مشتركة للتعامل مع LLMs، إدارة الذاكرة (Memory Management)، تسجيل الأحداث (Logging)، معالجة الأخطاء (Error Handling).

3.  **Database (PostgreSQL):**
    *   لتخزين بيانات المستخدم، المنتجات، الحملات الإعلانية (الخطط، النصوص، الأفكار)، ونتائج التحليلات (في المستقبل).
    *   استخدام SQLAlchemy مع Alembic لإدارة الـ Migrations.

4.  **Frontend (React + Tailwind CSS):**
    *   واجهة مستخدم تفاعلية للمستخدمين لإدخال معلومات المنتج وعرض مخرجات الوكلاء.
    *   استخدام Tailwind CSS لتصميم سريع وجميل.
    *   التواصل مع الـ Backend عبر API Gateway.

5.  **Queue/Message Broker (مثال: RabbitMQ أو Redis Streams):**
    *   **للتواصل بين الوكلاء:** لضمان قابلية التوسع وفصل الاهتمامات، سيتواصل الوكلاء بشكل غير متزامن عبر قائمة انتظار الرسائل. عندما يكمل وكيل مهمته، يرسل رسالة إلى قائمة الانتظار، ويستقبلها الوكيل التالي.
    *   **المعالجة الخلفية (Background Processing):** مهام توليد المحتوى قد تستغرق وقتًا، لذا يجب أن تتم في الخلفية.
    *   **في MVP:** يمكن البدء بتواصل مباشر بين خدمات FastAPI أو استخدام Redis بسيط كـ Queue، ثم التوسع إلى RabbitMQ أو Kafka لاحقًا.

#### 1.4.2. تدفق العمل (MVP Scenario)

1.  **المستخدم:** يدخل اسم المنتج، الوصف، السعر، الجمهور المستهدف عبر واجهة المستخدم (React).
2.  **Frontend:** يرسل البيانات إلى API Gateway.
3.  **API Gateway:** يوجه الطلب إلى Agent Orchestrator Service.
4.  **Agent Orchestrator Service:**
    *   يستقبل البيانات.
    *   يرسل مهمة إلى Marketing Research Agent Service (عبر Queue).
5.  **Marketing Research Agent Service:**
    *   يحلل البيانات باستخدام LLM.
    *   يستخرج USPs وتحليل السوق.
    *   يرسل النتائج إلى Agent Orchestrator Service (عبر Queue).
6.  **Agent Orchestrator Service:**
    *   يستقبل نتائج Marketing Research.
    *   يرسل مهمة إلى Copywriting Agent Service (عبر Queue).
7.  **Copywriting Agent Service:**
    *   يستخدم USPs ومعلومات المنتج لتوليد نصوص إعلانية، عناوين، CTAs.
    *   يرسل النتائج إلى Agent Orchestrator Service (عبر Queue).
8.  **Agent Orchestrator Service:**
    *   يستقبل نتائج Copywriting.
    *   يرسل مهمة إلى Creative Agent Service (عبر Queue).
9.  **Creative Agent Service:**
    *   يستخدم معلومات المنتج والنصوص لتوليد أفكار تصاميم وصور وفيديوهات (نصية).
    *   يرسل النتائج إلى Agent Orchestrator Service (عبر Queue).
10. **Agent Orchestrator Service:**
    *   يستقبل نتائج Creative.
    *   يرسل مهمة إلى Campaign Strategy Agent Service (عبر Queue).
11. **Campaign Strategy Agent Service:**
    *   يستخدم جميع المعلومات لتوليد خطة حملة إعلانية واستراتيجية.
    *   يرسل النتائج إلى Agent Orchestrator Service (عبر Queue).
12. **Agent Orchestrator Service:**
    *   يجمع جميع المخرجات من الوكلاء.
    *   يخزنها في PostgreSQL.
    *   يرسل النتائج المجمعة إلى API Gateway.
13. **API Gateway:** يرسل النتائج إلى Frontend.
14. **Frontend:** يعرض خطة الإعلان الكاملة، النصوص، أفكار التصاميم والفيديو، والاستراتيجية للمستخدم.

#### 1.4.3. قرارات تقنية وهندسية

*   **Python + FastAPI:** اختيار ممتاز للـ Backend نظرًا لأدائه العالي، سهولة الاستخدام، ودعم الـ Asynchronous operations، وهو مثالي لخدمات الـ Microservices والتعامل مع LLMs.
*   **React + Tailwind CSS:** يوفر تجربة تطوير سريعة ومرنة للواجهة الأمامية، مع تصميمات عصرية وقابلة للتخصيص.
*   **PostgreSQL:** قاعدة بيانات علائقية قوية ومفتوحة المصدر، تدعم قابلية التوسع وتوفر موثوقية عالية لتخزين بيانات الحملات والمنتجات.
*   **Modular Architecture:** كل وكيل (Agent) سيكون وحدة مستقلة (أو خدمة منفصلة) لضمان سهولة التطوير، الاختبار، والنشر، بالإضافة إلى قابلية التوسع بشكل مستقل.
*   **Scalability:** استخدام FastAPI و Event-Driven Architecture (عبر Queue) يضمن قابلية التوسع الأفقي لكل خدمة بشكل مستقل، مما يسمح بالتعامل مع أعداد كبيرة من الطلبات.
*   **Open-source LLMs (Qwen, DeepSeek, Llama):** الالتزام بالنماذج مفتوحة المصدر يقلل التكاليف في مرحلة MVP ويمنحنا مرونة أكبر في التخصيص والتحكم. سيتم استخدام مكتبات مثل `transformers` أو `langchain` أو `llama-cpp-python` للتفاعل مع هذه النماذج.
*   **لا خدمات مدفوعة في MVP:** سيتم تجنب استخدام خدمات سحابية مدفوعة (مثل Vertex AI أو OpenAI API) في MVP، والاعتماد على الحلول مفتوحة المصدر أو المجانية قدر الإمكان. يمكن تشغيل النماذج مفتوحة المصدر محليًا أو على خوادم بحد أدنى من التكلفة.
*   **جاهزية SaaS عالمي:** التصميم القائم على Microservices و Event-Driven Architecture، واستخدام تقنيات مفتوحة المصدر، يضع أساسًا قويًا للتحول إلى SaaS عالمي في المستقبل.

### 1.5. هيكل المشروع المقترح (MVP)

```
AdGeniusAI/
├── backend/                         # مشروع FastAPI للـ Backend
│   ├── app/                         # تطبيق FastAPI الرئيسي
│   │   ├── __init__.py
│   │   ├── main.py                  # نقطة الدخول الرئيسية للـ API Gateway
│   │   ├── api/                     # وحدات API للـ Gateway
│   │   │   ├── __init__.py
│   │   │   └── v1/
│   │   │       ├── __init__.py
│   │   │       └── endpoints/
│   │   │           ├── __init__.py
│   │   │           └── ad_generation.py # endpoint لتوليد الإعلانات
│   │   ├── core/                    # إعدادات وتكوينات أساسية
│   │   │   ├── __init__.py
│   │   │   ├── config.py            # إعدادات المشروع (مثل DB URL, LLM paths)
│   │   │   └── security.py          # المصادقة والترخيص
│   │   ├── db/                      # إعدادات قاعدة البيانات
│   │   │   ├── __init__.py
│   │   │   ├── database.py          # اتصال قاعدة البيانات
│   │   │   ├── models.py            # تعريفات نماذج SQLAlchemy
│   │   │   └── migrations/          # ملفات Alembic migrations
│   │   ├── schemas/                 # Pydantic schemas للمدخلات والمخرجات
│   │   │   ├── __init__.py
│   │   │   └── ad_request.py
│   │   ├── services/                # منطق الأعمال (Business Logic) والـ Orchestration
│   │   │   ├── __init__.py
│   │   │   └── agent_orchestrator.py # خدمة تنسيق الوكلاء
│   │   ├── agents/                  # وحدات الوكلاء (يمكن فصلها لاحقًا كـ microservices)
│   │   │   ├── __init__.py
│   │   │   ├── marketing_research_agent.py
│   │   │   ├── copywriting_agent.py
│   │   │   ├── creative_agent.py
│   │   │   ├── campaign_strategy_agent.py
│   │   │   └── analytics_agent.py   # (MVP: تصميم نظري أو توصيات عامة)
│   │   └── utils/                   # أدوات مساعدة (مثل LLM handler)
│   │       ├── __init__.py
│   │       └── llm_handler.py       # واجهة موحدة للتعامل مع LLMs المختلفة
│   ├── tests/                       # اختبارات الـ Backend
│   ├── requirements.txt             # تبعيات Python
│   └── Dockerfile                   # Dockerfile للـ Backend
├── frontend/                        # مشروع React للـ Frontend
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── pages/
│   │   │   └── AdGenerationPage.jsx
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   ├── package.json                 # تبعيات Node.js
│   ├── tailwind.config.js           # إعدادات Tailwind CSS
│   ├── postcss.config.js
│   └── Dockerfile                   # Dockerfile للـ Frontend
├── docker-compose.yml               # لـ Docker Compose لتشغيل كل المكونات
├── .gitignore
└── README.md                        # وثائق المشروع

### 1.6. المراجع

[1] [ATH-MaaS/Agentic-ADK - GitHub](https://github.com/AIDC-AI/Agentic-ADK)
[2] [alibaba/spring-ai-alibaba - GitHub](https://github.com/alibaba/spring-ai-alibaba)
[3] [google-marketing-solutions/vigenair - GitHub](https://github.com/google-marketing-solutions/vigenair)
[4] [google-marketing-solutions/adios - GitHub](https://github.com/google-marketing-solutions/adios)
