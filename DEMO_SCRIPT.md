# 🎤 Live Demo Script: Tech Products API
**Duration:** 8-10 minutes | **Speaker:** Sarah Rose Hassan

---

## 📋 Pre-Demo Checklist (5 min before)
- [ ] Close all unnecessary browser tabs/windows
- [ ] Open Terminal in project directory
- [ ] Ensure server is NOT running (`lsof -ti:8000 | xargs kill -9`)
- [ ] Deactivate any active virtual environments (`deactivate`)
- [ ] Open GitHub repository page in browser (tab 1)
- [ ] Have `http://127.0.0.1:8000/docs` ready to open (tab 2)
- [ ] Test screen sharing visibility
- [ ] Prepare water/clear throat

---

## 🎬 Demo Flow (8-10 minutes)

### **PART 1: Introduction & Problem Statement (1 min)**

**[SCREEN: GitHub Repository]**

> "Hi everyone! Today I'm demonstrating a REST API backend that solves a real-world problem: managing product inventory for an e-commerce platform.
>
> Imagine you're building an online tech store. You need a backend that can:
> - Serve product data to mobile apps and websites
> - Filter items by category in real-time
> - Look up specific products instantly
>
> This API does exactly that using modern Python technologies."

**[Show repository README quickly]**

> "Our complete documentation is here on GitHub with step-by-step tutorials, but let me show you how it works live."

---

### **PART 2: Project Overview & Tech Stack (1.5 min)**

**[SCREEN: Terminal - Navigate to project]**

```bash
cd /Users/sarah/Coding/fastapi-data-demo
ls -la
```

> "Let's look at our project structure. We have:
> - `main.py` - Our FastAPI application with three endpoints
> - `data.csv` - Sample product data (simulating a database)
> - `requirements.txt` - Our dependencies: FastAPI, Uvicorn, and Pandas
> - Automation scripts for easy setup on Mac, Linux, and Windows"

**[Show data.csv quickly]**

```bash
head -n 5 data.csv
```

> "Our CSV contains 10 tech products with IDs, names, prices, categories, and stock counts. In production, this would be a real database like PostgreSQL."

---

### **PART 3: Quick Setup Demo (1 min)**

**[SCREEN: Terminal]**

> "One of our design goals was **usability**. Instead of multiple manual commands, we created one-click setup:"

```bash
cat setup.sh
```

> "This script creates a virtual environment, activates it, and installs all dependencies. Let me show you how easy it is to start:"

```bash
./start.sh
```

**[Wait for server to start - show output]**

> "In just seconds, our server is running on port 8000. Notice the helpful messages telling users exactly where to go."

---

### **PART 4: Live API Demonstration (3.5 min)**

**[SCREEN: Browser - Navigate to http://127.0.0.1:8000/docs]**

> "FastAPI automatically generates this interactive documentation called Swagger UI. Let me demonstrate our three endpoints:"

#### **Endpoint 1: Get All Items**

**[Click GET /items, Try it out, Execute]**

> "First, we can retrieve all products. Watch the server response in real-time...
>
> **[Point to results]**
>
> Perfect! We get all 10 products with complete details. Notice the JSON format - this is what mobile apps and websites would consume. The response code is 200, meaning success."

#### **Endpoint 2: Filter by Category**

**[Scroll to category parameter]**

> "Now let's say a customer only wants to see Audio products. We use a query parameter:"

**[Type: Audio, Execute]**

> "See how Pandas filters the data in milliseconds? Only the Sony headphones appear because it's our only Audio category item. This demonstrates how query parameters enable dynamic filtering."

#### **Endpoint 3: Get Specific Item**

**[Scroll to GET /items/{item_id}]**

> "Finally, path parameters let us look up specific products. Let's search for item 106:"

**[Click Try it out, Enter: 106, Execute]**

> "And we get the Apple Watch details instantly. If I try an invalid ID like 999..."

**[Enter: 999, Execute]**

> "We get a proper 404 error with a helpful message. This is **robust error handling** - essential for production APIs."

---

### **PART 5: Code Walkthrough (2 min)**

**[SCREEN: VS Code or Terminal with main.py]**

```bash
cat main.py
```

> "Let me quickly explain the code architecture:
>
> **[Scroll through main.py]**
>
> 1. **Lines 1-9:** We initialize FastAPI with metadata for documentation
> 2. **Lines 11-15:** Data loading happens once at startup - not on every request. This is a performance optimization
> 3. **Lines 17-20:** Our root endpoint returns a simple welcome message
> 4. **Lines 22-31:** The `/items` endpoint handles both 'get all' and 'filter by category' using an optional parameter
> 5. **Lines 33-40:** The specific item lookup uses a path parameter and includes proper error handling
>
> Notice how clean and readable this code is - FastAPI's decorator pattern makes REST APIs intuitive."

---

### **PART 6: Real-World Applications (0.5 min)**

**[SCREEN: Back to browser/terminal]**

> "This architecture scales to real applications:
> - E-commerce platforms like Shopify
> - Mobile app backends
> - Microservices in large systems
>
> You'd simply swap the CSV for a database, add authentication, and deploy to the cloud."

---

### **PART 7: Cleanup & Questions (0.5 min)**

**[SCREEN: Terminal]**

```bash
# Press Ctrl+C to stop server
deactivate
```

> "Cleanup is just as simple - stop the server and deactivate the environment.
>
> Key takeaways:
> 1. ✅ FastAPI makes REST APIs simple and fast
> 2. ✅ Automatic documentation saves development time
> 3. ✅ One-command setup improves usability
> 4. ✅ Proper error handling is essential
>
> The complete code, documentation, and setup instructions are on GitHub. Happy to answer questions!"

---

## 🎯 Teaching Tips

### **Communication Best Practices:**
1. **Speak clearly and pace yourself** - Not too fast, especially on technical terms
2. **Make eye contact** with camera (not screen)
3. **Use analogies** - "like a menu in a restaurant" for API endpoints
4. **Point and highlight** - Use cursor to guide attention
5. **Pause after key points** - Let information sink in
6. **Anticipate questions** - "You might be wondering why..."

### **Technical Depth Demonstrations:**
- **Show actual code** (not just UI)
- **Explain WHY not just WHAT** (e.g., why virtual environments matter)
- **Demonstrate error handling** (show 404 response)
- **Discuss performance** (mention why data loads once)
- **Connect to real-world** (mention production considerations)

### **Handling Q&A:**
- "Great question! Let me show you..." → **Demo it live**
- "That's beyond today's scope, but..." → **Reference docs**
- "I'm not 100% sure, but I believe..." → **Honesty builds trust**

---

## ⚠️ Common Pitfalls to Avoid

1. ❌ **Don't rush** - Speak slower than you think necessary
2. ❌ **Don't read slides** - Engage naturally
3. ❌ **Don't say "um" repeatedly** - Pause instead
4. ❌ **Don't show unprepared errors** - Test everything beforehand
5. ❌ **Don't go over time** - Practice with a timer

---

## 🔄 Backup Plans

**If server won't start:**
- Show pre-recorded screenshots
- Walk through code instead
- Explain what SHOULD happen

**If internet fails:**
- Everything runs locally (no internet needed!)
- Use localhost, not cloud services

**If time runs short:**
- Skip "Next Steps" section
- Focus on live demo over code walkthrough

---

## 📊 Self-Evaluation Checklist

After your demo, assess yourself:

**Technical Content (10 pts):**
- [ ] Explained REST API concepts clearly
- [ ] Demonstrated all three endpoints
- [ ] Showed error handling
- [ ] Connected to real-world applications
- [ ] Explained code architecture

**Demo Structure (6 pts):**
- [ ] Clear introduction with problem statement
- [ ] Logical flow (setup → demo → code → applications)
- [ ] Stayed within time limit
- [ ] Smooth transitions between sections

**Teaching Quality (4 pts):**
- [ ] Spoke clearly and confidently
- [ ] Used analogies and examples
- [ ] Engaged audience with questions
- [ ] Made eye contact (with camera)

---

## 🎓 Grading Rubric Alignment

| Criterion | How Demo Addresses It |
|-----------|----------------------|
| **Technical Content & Depth (10 pts)** | Live code walkthrough, architecture explanation, real-world applications, error handling demo |
| **Demo Structure & Quality (6 pts)** | Clear 7-part structure, logical flow, time management, smooth transitions |
| **Teaching Quality & Communication (4 pts)** | Clear explanations, analogies, pacing, engagement, eye contact |

**Target Score: 20/20**
