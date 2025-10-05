### **1. What are the main differences between HTTP, MQTT, and CoAP?**

| Feature     | **HTTP**              | **MQTT**                    | **CoAP**                                               |
| ----------- | --------------------- | --------------------------- | ------------------------------------------------------ |
| Transport   | TCP                   | TCP                         | UDP                                                    |
| Model       | Request–Response      | Publish–Subscribe (Broker)  | Request–Response (like HTTP but lighter) (lightweight) |
| Overhead    | Heavy (Headers)       | Very light                  | Very light                                             |
| Use Case    | Web APIs, File upload | IoT sensors, real-time data | Constrained devices (low power, low bandwidth)         |
| Reliability | High                  | Adjustable (QoS levels)     | Optional (Confirmable messages)                        |

---

### **2. Which protocol would you choose for:**

| Scenario                                  | Best Protocol | Reason                                            |
| ----------------------------------------- | ------------- | ------------------------------------------------- |
| **Sending temperature data every second** | **MQTT**      | Lightweight + efficient for continuous publishing |
| **Controlling a smart bulb (on/off)**     | **CoAP **     | CoAP if very low power device                     |
| **Uploading a large file**                | **HTTP**      | Supports large payloads + file transfer           |

---

### **3. Explain QoS levels (0, 1, 2) in MQTT and give one use case for each.**

| QoS Level                 | Guarantee                              | Use Case                                               |
| ------------------------- | -------------------------------------- | ------------------------------------------------------ |
| **QoS 0 – At most once**  | Send and forget (no acknowledgment)    | Live sensor data like temperature (loss is acceptable) |
| **QoS 1 – At least once** | Guaranteed delivery but may duplicate  | Turning a smart bulb ON/OFF                            |
| **QoS 2 – Exactly once**  | No loss, no duplicates (most reliable) | Banking/payment message                                |

---

### **4. Why does CoAP use UDP instead of TCP?**

Because **UDP is faster, lighter, and requires fewer resources** — ideal for **low-power IoT devices**.

- No connection setup like TCP → **saves time and battery**
    
- Smaller packet size → No Header Like HTTP 
    
- CoAP **adds its own reliability mechanism** (Confirmable / Non-confirmable messages), so it doesn’t fully rely on TCP.


---

### **5. Why is HTTP still widely used even though MQTT and CoAP are lighter for IoT?**

- **HTTP is universal** → Supported by all web servers, browsers, cloud services.
    
- **Easy to debug & develop** → Can be tested via **browser or Postman**.
    
- **Firewall-friendly** → Uses port 80/443 (open everywhere).
    
- **REST APIs & Backend Integration** → Most cloud platforms provide REST endpoints, not MQTT brokers.

 _So even if HTTP is heavier, it’s still the simplest and most compatible option in many cases._

---
