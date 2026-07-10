# AdGenius AI: منصة تسويق وإعلانات بالذكاء الاصطناعي

## ملخص المشروع

AdGenius AI هي منصة ذكاء اصطناعي متكاملة تعمل كفريق تسويق وإعلانات للشركات والأفراد. تهدف المنصة إلى أتمتة مهام التسويق والإعلان من خلال نظام Multi-Agent متطور، يقدم حلولاً شاملة بدءًا من تحليل السوق وحتى تحليل أداء الحملات.

## الميزات الرئيسية (MVP)

*   **نظام Multi-Agent:** يتكون من 5 وكلاء متخصصين:
    *   **Marketing Research Agent:** تحليل السوق والمنافسين والجمهور، استخراج نقاط البيع الفريدة (USPs)، تحليل SWOT، وتحديد الرسالة الجوهرية.
    *   **Copywriting Agent:** إنشاء 5 نسخ إعلانية متنوعة (عاطفية، تعليمية، عرض-محرك، دليل اجتماعي، قصيرة ومباشرة) مع عناوين ونصوص رئيسية وعبارات تحث المستخدم على اتخاذ إجراء (CTAs).
    *   **Creative Agent:** اقتراح 3 أفكار لتصاميم صور إعلانية مفصلة، و2 سيناريو لفيديو قصير (Reels/TikTok) مع المشاهد والمحتوى والخاتمة والمؤثرات الصوتية.
    *   **Campaign Strategy Agent:** بناء خطة حملة متكاملة تشمل الأهداف، مزيج المنصات، تكتيكات الاستهداف، هيكل الحملة، توصيات الميزانية، خارطة الطريق، ومؤشرات الأداء الرئيسية (KPIs).
    *   **Analytics Agent:** تحليل نقدي لخطة الحملة والمخرجات، تقييم التماسك، تحديد المخاطر، توصيات التحسين الفوري، استراتيجية الاختبار (A/B Testing)، وتوقعات الأداء.
*   **واجهة مستخدم تفاعلية:** تسمح للمستخدم بإدخال بيانات المنتج وعرض جميع مخرجات الوكلاء بشكل منظم.

## المتطلبات التقنية

*   **Backend:** Python + FastAPI
*   **Frontend:** React + Tailwind CSS
*   **Database:** PostgreSQL
*   **Architecture:** Modular + Scalable Multi-Agent System
*   **AI:** دعم النماذج مفتوحة المصدر (Qwen, DeepSeek, Llama) عبر واجهة OpenAI-compatible API.

## تصميم Architecture

يعتمد المشروع على بنية **Microservices** لضمان قابلية التوسع والمرونة، مع التركيز على نمط **Event-Driven Architecture** للتواصل بين الوكلاء. يتكون النظام من المكونات الرئيسية التالية:

1.  **Gateway / API Gateway (FastAPI):** نقطة الدخول الوحيدة لجميع طلبات الواجهة الأمامية، مسؤول عن المصادقة والترخيص، وتوجيه الطلبات إلى الخدمات الخلفية المناسبة.
2.  **Backend Services (FastAPI + Python):** كل وكيل (Agent) هو وحدة منطقية داخل خدمة FastAPI، قابلة للفصل لاحقًا كـ microservice مستقلة. `AgentOrchestratorService` ينسق تدفق العمل بين الوكلاء.
3.  **Database (PostgreSQL):** لتخزين بيانات المستخدم، المنتجات، الحملات الإعلانية (الخطط، النصوص، الأفكار)، ونتائج التحليلات. يتم استخدام SQLAlchemy مع Alembic لإدارة الـ Migrations.
4.  **Frontend (React + Tailwind CSS):** واجهة مستخدم تفاعلية وجذابة، تتواصل مع الـ Backend عبر API Gateway.
5.  **Queue/Message Broker (مستقبلاً):** لضمان قابلية التوسع وفصل الاهتمامات، سيتواصل الوكلاء بشكل غير متزامن عبر قائمة انتظار الرسائل. في MVP، يتم التواصل بشكل مباشر داخل `AgentOrchestrator`.

## هيكل المشروع

```
AdGeniusAI/
├── backend/                         # مشروع FastAPI للـ Backend
│   ├── app/                         # تطبيق FastAPI الرئيسي
│   │   ├── api/                     # وحدات API للـ Gateway
│   │   │   └── v1/
│   │   │       └── endpoints/
│   │   │           └── ad_generation.py # endpoint لتوليد الإعلانات
│   │   ├── core/                    # إعدادات وتكوينات أساسية (config.py)
│   │   ├── db/                      # إعدادات قاعدة البيانات (database.py, models.py, migrations/)
│   │   ├── schemas/                 # Pydantic schemas للمدخلات والمخرجات
│   │   ├── services/                # منطق الأعمال والـ Orchestration (agent_orchestrator.py)
│   │   ├── agents/                  # وحدات الوكلاء (marketing_research_agent.py, copywriting_agent.py, creative_agent.py, campaign_strategy_agent.py, analytics_agent.py)
│   │   └── utils/                   # أدوات مساعدة (llm_handler.py)
│   │   ├── main.py                  # نقطة الدخول الرئيسية للـ FastAPI
│   ├── requirements.txt             # تبعيات Python
│   ├── .env                         # متغيرات البيئة (LLM_API_BASE, LLM_API_KEY, LLM_MODEL)
│   ├── alembic.ini                  # إعدادات Alembic
│   └── Dockerfile                   # Dockerfile للـ Backend
├── frontend/                        # مشروع React للـ Frontend
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   │   └── AdGenerationPage.jsx # صفحة توليد الإعلانات
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json                 # تبعيات Node.js
│   ├── tailwind.config.js           # إعدادات Tailwind CSS
│   └── Dockerfile                   # Dockerfile للـ Frontend
├── docker-compose.yml               # لـ Docker Compose لتشغيل كل المكونات
└── .gitignore
```

## كيفية التشغيل محلياً (باستخدام Docker Compose)

للتشغيل، تأكد من تثبيت Docker و Docker Compose على نظامك.

1.  **استنساخ المستودع:**
    ```bash
    git clone https://github.com/Terex2/AdGeniusAI.git
    cd AdGeniusAI
    ```

2.  **إعداد ملف `.env`:**
    انتقل إلى مجلد `backend` وقم بإنشاء ملف `.env` (إذا لم يكن موجوداً) بالمعلومات التالية:
    ```
    PROJECT_NAME="AdGenius AI"
    DATABASE_URL="postgresql://user:password@db:5432/adgenius_db"
    LLM_API_BASE="http://host.docker.internal:11434/v1" # مثال لـ Ollama
    LLM_API_KEY="ollama"
    LLM_MODEL="llama3" # أو أي نموذج مفتوح المصدر مثل qwen, deepseek
    ```
    *ملاحظة:* `LLM_API_BASE` هنا يشير إلى `Ollama` الذي يعمل على جهازك المحلي. تأكد من تشغيل `Ollama` وتنزيل النموذج الذي تختاره (مثال: `ollama run llama3`).

3.  **تشغيل Docker Compose:**
    من المجلد الرئيسي للمشروع (`AdGeniusAI/`)، قم بتشغيل الأمر التالي:
    ```bash
    docker-compose up --build
    ```
    سيقوم هذا الأمر ببناء صور Docker وتشغيل الخدمات (قاعدة البيانات، Backend، Frontend).

4.  **إعداد قاعدة البيانات (Migrations):**
    بعد تشغيل الخدمات، ستحتاج إلى تطبيق الـ migrations على قاعدة البيانات. افتح نافذة طرفية جديدة وادخل إلى حاوية الـ `backend`:
    ```bash
    docker-compose exec backend bash
    ```
    ثم قم بتشغيل الـ migrations:
    ```bash
    alembic revision --autogenerate -m "Create Campaign table"
    alembic upgrade head
    exit
    ```

5.  **الوصول إلى التطبيق:**
    *   الـ Backend API سيكون متاحاً على: `http://localhost:8000`
    *   الـ Frontend سيكون متاحاً على: `http://localhost:3000`

    افتح متصفحك وتوجه إلى `http://localhost:3000` لبدء استخدام AdGenius AI.

## المراجع

[1] [ATH-MaaS/Agentic-ADK - GitHub](https://github.com/AIDC-AI/Agentic-ADK)
[2] [alibaba/spring-ai-alibaba - GitHub](https://github.com/alibaba/spring-ai-alibaba)
[3] [google-marketing-solutions/vigenair - GitHub](https://github.com/google-marketing-solutions/vigenair)
[4] [google-marketing-solutions/adios - GitHub](https://github.com/google-marketing-solutions/adios)
