# 🔧 Render Advanced Configuration - Cấu Hình Nâng Cao

## 🎯 Cấu Hình Nâng Cao cho Performance Tốt Hơn

### 1. Plan Selection

#### Free Plan (Miễn Phí)
**Specs:**
- CPU: 0.1 (share)
- RAM: 512 MB
- Storage: 1 GB
**Giới Hạn:**
- Sleep sau 15 phút không hoạt động
- cold start time: ~30s
- Không đảm bảo uptime

**Phù Hợp Cho:**
- Testing bot
- Development
- Bot hoạt động thấp

#### Starter Plan ($7/tháng)
**Specs:**
- CPU: 0.5 (share)  
- RAM: 512 MB
- Storage: 10 GB
**Lợi Ích:**
- Không sleep (24/7)
- cold start time: ~10s
- Guaranteed uptime 99%

**Phù Hợp Cho:**
- Bot production
- High traffic
- Quan trọng

#### Standard Plan ($25/tháng)
**Specs:**
- CPU: 1 (dedicated)
- RAM: 2 GB
- Storage: 25 GB
**Lợi Ích:**
- Performance tốt hơn
- Hỗ trợ database
- Better logs retention

**Phù Hợp Cho:**
- Bot lớn
- Heavy processing
- Enterprise

---

### 2. Region Selection

#### Singapore (Khuyên Dùng Cho Việt Nam)
- **Lợi ích**: Độ trễ thấp (10-50ms)
- **Phù hợp**: Bot hoạt động chủ yếu ở Việt Nam

#### Oregon (Mỹ West)
- **Lợi ích**: Độ trễ trung bình (50-150ms)
- **Phù hợp**: Bot quốc tế

#### Frankfurt (Châu Âu)
- **Lợi ích**: Độ trễ trung bình (50-150ms)
- **Phù hợp**: Bot hoạt động ở Châu Âu

---

### 3. Environment Variables Nâng Cao

### 3.1 Performance Variables
```yaml
PYTHON_VERSION: "3.9.0"
PYTHONUNBUFFERED: "1"  # Disable Python output buffering
TZ: "Asia/Ho_Chi_Minh"    # Timezone Việt Nam
```

### 3.2 Logging Variables
```yaml
LOG_LEVEL: "INFO"
DISCORD_LOG_LEVEL: "WARNING"  # Giảm log spam
```

### 3.3 Bot Variables
```yaml
BOT_SHARDING: "false"     # Nếu bot lớn >250 servers
BOT_INTENTS: "all"        # Intents Discord
```

---

### 4. Health Checks

### 4.1 Enable Health Check
```yaml
healthCheckPath: /
healthCheckInterval: 30
autoDeploy: false  # Tắt auto deploy để control tốt hơn
```

### 4.2 Custom Health Check
Thêm vào `start.py`:
```python
# Simple health check endpoint
from flask import Flask
app = Flask(__name__)

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    # Start health check server in background
    import threading
    def run_server():
        app.run(host='0.0.0.0', port=8000, port=5000)
    
    health_thread = threading.Thread(target=run_server, daemon=True)
    health_thread.start()
    
    # Start bot
    import bot
```

---

### 5. Database Options (Nếu Cần)

### 5.1 Render PostgreSQL (Free)
- 1 GB storage
- 90 connections limit
- Auto backup

### 5.2 Render Redis (Free)
- 25 MB storage
- Persistent connections
- Good for caching

### 5.3 SQLite (Free)
- File-based database
- Limited scalability
- Phù hợp cho users.json

---

### 6. Scaling Strategies

### 6.1 Horizontal Scaling
- Tạo nhiều services
- Load balancing
- Region distribution

### 6.2 Vertical Scaling
- Upgrade plan
- Increase CPU/RAM
- Better performance

### 6.3 Bot Sharding
- Split bot thành multiple shards
- Each shard handles subset of servers
- Better for large bots (>1000 servers)

---

### 7. Monitoring & Alerts

### 7.1 Render Metrics
- CPU usage
- Memory usage
- Response time
- Error rates

### 7.2 Custom Monitoring
```python
# Add monitoring to bot.py
import psutil
import time

def log_metrics():
    while True:
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        print(f"CPU: {cpu}%, Memory: {memory}%")
        time.sleep(60)  # Log mỗi phút

# Start trong background
import threading
monitor_thread = threading.Thread(target=log_metrics, daemon=True)
monitor_thread.start()
```

### 7.3 External Monitoring
- **Uptime Robot**: Monitor bot uptime
- **Prometheus**: Collect metrics
- **Grafana**: Visualize metrics

---

### 8. Security Configuration

### 8.1 Secrets Management
```yaml
envVars:
  - key: DISCORD_TOKEN
    type: secret  # Bảo mật, không hiển thị
    sync: false  # Không sync với GitHub
    
  - key: ADMIN_IDS
    type: secret
    sync: false
```

### 8.2 Network Security
- HTTPS tự động
- SSL certificate
- Firewall rules

### 8.3 Access Control
- IP whitelist (Render Business plan)
- VPC peering
- Private services

---

### 9. Optimization Tips

### 9.1 Build Optimization
```yaml
# Caching dependencies
buildCommand: pip install -r requirements.txt --cache-dir
```

### 9.2 Startup Optimization
```python
# Lazy imports trong start.py
import sys
import os

# Chỉ import khi cần thiết
def import_bot():
    import bot
    return bot

# Sử dụng lazy loading
if __name__ == "__main__":
    bot = import_bot()
    bot.run(os.environ.get("DISCORD_TOKEN"))
```

### 9.3 Memory Optimization
```python
# Giảm memory usage
import gc
import os

# Force garbage collection
gc.collect()

# Set memory limit (Linux)
import resource
resource.setrlimit(resource.RLIMIT_AS, (512 * 1024 * 1024, 512 * 1024 * 1024))
```

---

### 10. Deployment Strategies

### 10.1 Blue-Green Deployment
- Deploy new version
- Test new version
- Switch traffic
- Rollback if needed

### 10.2 Canary Deployment
- Deploy to subset of users
- Monitor metrics
- Gradual rollout
- Full deployment

### 10.3 Rolling Update
- Update instance by instance
- Zero downtime
- Auto rollback on failure

---

## 🎯 Advanced Config cho Bot Cụ Thể

### Discord Bot Optimization
```yaml
# render.yaml nâng cao
services:
  - type: web
    name: super-ultimate-bot-3
    env: python
    buildCommand: pip install -r requirements.txt --no-cache-dir
    startCommand: gunicorn -w 1 -b 0.0.0.0:$PORT start:app
    envVars:
      - key: DISCORD_TOKEN
        type: secret
      - key: ADMIN_IDS
        type: secret
      - key: PYTHON_VERSION
        value: 3.9.0
      - key: TZ
        value: Asia/Ho_Chi_Minh
      - key: PYTHONUNBUFFERED
        value: "1"
    plan: starter
    region: Singapore
    healthCheckPath: /health
    autoDeploy: false
```

### Custom Start Script
```python
# start.py nâng cao
import os
import sys
import logging
from multiprocessing import cpu_count

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Optimize Gunicorn workers
workers = max(2, cpu_count() * 2 + 1)

if __name__ == "__main__":
    import bot
    bot.run(os.environ.get("DISCORD_TOKEN"))
```

---

## 🚀 Performance Tuning

### Discord API Rate Limits
- Respect Discord rate limits (50 requests/second)
- Implement bucket algorithm
- Use session pooling

### Database Optimization
- Use connection pooling
- Optimize queries
- Index frequently accessed data

### Memory Optimization
- Use generators instead of lists
- Process large files in chunks
- Clear cache periodically

---

## 🎯 Configuration Checklist

- [ ] Chọn appropriate plan
- [ ] Select optimal region
- [ ] Configure all environment variables
- [ ] Set up health checks
- [ ] Enable monitoring
- [ ] Configure scaling rules
- [ ] Set up alerts
- [ ] Test failover
- [ ] Document configuration
- [ ] Backup important data

---

**Super Ultimate Bot 3.0 - Advanced Configuration**

Made with ❤️ by zawng dep chai