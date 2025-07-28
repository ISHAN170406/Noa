# Noa - Advanced Modular AI Companion & Smart Assistant

<div align="center">
  <img src="https://img.shields.io/badge/Version-1.0.0-blue.svg" alt="Version">
  <img src="https://img.shields.io/badge/Python-3.8+-green.svg" alt="Python">
  <img src="https://img.shields.io/badge/Node.js-16+-yellow.svg" alt="Node.js">
  <img src="https://img.shields.io/badge/License-MIT-red.svg" alt="License">
</div>

A sophisticated, modular AI companion that combines the conversational abilities of a personal assistant with the functionality of smart home devices like Alexa, enhanced with advanced memory retention and customizable hardware modules.

## 🤖 What is Noa?

Noa is a comprehensive AI companion system that goes beyond simple conversation to provide:

- **🏠 Alexa-equivalent functionality** with smart home integration and voice commands
- **🧠 Advanced memory retention** using RAG (Retrieval Augmented Generation) for personalized, context-aware interactions
- **🔧 Modular hardware design** - easily expandable with cameras, wheels, sensors, and other components
- **🎤 Voice-based interactions** using advanced speech recognition and text-to-speech
- **😊 Dynamic facial expressions** displayed on connected hardware (ESP32)
- **👤 Personalized conversation styles** adapted for different user types (Kids, Seniors, Tech enthusiasts)
- **💻 Cross-platform desktop interface** for easy management and setup

## 🎯 Why Choose Noa Over Traditional Assistants?

### 🏠 Smart Home Integration (Alexa Alternative)
- **Voice commands** for controlling lights, thermostats, music, and smart devices
- **Weather updates, news briefings, and general information queries**
- **Timer and alarm management** with personalized notifications
- **Music streaming and podcast control** with voice commands
- **Calendar management** and appointment scheduling
- **Shopping lists and reminders** with intelligent suggestions
- **Smart home automation** with custom routines and scenes

### 🧠 Advanced Memory & Learning (RAG-Powered)
- **Long-term memory retention** - remembers past conversations, preferences, and important details
- **Contextual understanding** - builds on previous interactions for more meaningful conversations
- **Personal knowledge base** - learns about your habits, interests, and needs over time
- **Intelligent recommendations** based on historical interactions and preferences
- **Conversation continuity** across sessions with seamless context switching

### 🔧 Modular Hardware System
- **📷 Camera modules** for visual recognition, security monitoring, and video calls
- **🛞 Mobility modules** with wheels for autonomous movement and following
- **🌡️ Sensor arrays** including temperature, humidity, motion, and proximity sensors
- **🖥️ Display modules** for visual information, charts, and interactive interfaces
- **🔊 Speaker upgrades** for enhanced audio quality and multi-room audio
- **🏠 IoT integration** with custom sensors and actuators for specialized applications

## 👥 Perfect For Every User Type

### For Children 🧒
- **Educational companion** with visual learning through camera integration
- **Interactive games** using movement and gesture recognition
- **Safety monitoring** with camera and sensor-based child supervision
- **Mobile storytelling** - follows children around for immersive story experiences

### For Seniors 👴
- **Health monitoring** through integrated sensors and camera analysis
- **Medication reminders** with visual confirmation via camera
- **Fall detection** using motion sensors and camera analysis
- **Video calling** with family members through integrated camera system
- **Home security** with mobile monitoring capabilities

### For Tech Enthusiasts 👨‍💻
- **Development platform** for custom modules and integrations
- **IoT hub** connecting and managing various smart devices
- **Data collection and analysis** from multiple sensor inputs
- **Custom automation** with programming interfaces and APIs

## 🛠️ Technology Stack

### Core AI & Processing
- **AI Engine**: Google Gemini 2.0 Flash for conversation and expression generation
- **Memory System**: RAG implementation with vector databases for long-term retention
- **Speech Recognition**: Google Speech Recognition API with offline backup
- **Text-to-Speech**: Piper TTS with high-quality neural voices
- **Computer Vision**: OpenCV integration for camera modules

### Hardware & Communication
- **Main Controller**: ESP32 with expandable GPIO for modules
- **Communication**: Serial/Bluetooth/WiFi for multi-device coordination
- **Modular Interface**: Standardized connectors for easy hardware expansion
- **Power Management**: Smart battery management for mobile operations

### Software Platform
- **Desktop Interface**: Electron.js with modern, responsive UI
- **Backend**: Python with asyncio for concurrent processing
- **Database**: Vector database for RAG memory system
- **API Layer**: RESTful APIs for third-party integrations

## 📋 Comprehensive Feature Set

### 🎙️ Voice Assistant Capabilities (Alexa-Equivalent)

| Feature | Command Example |
|---------|----------------|
| Smart Home Control | "Noa, turn off the living room lights" |
| Information Queries | "Noa, what's the weather forecast for tomorrow?" |
| Entertainment Control | "Noa, play my morning playlist" |
| Productivity | "Noa, add dentist appointment to my calendar" |
| Communication | "Noa, call mom" or "Noa, send a message to John" |
| Shopping & Commerce | "Noa, add milk to my shopping list" |
| News & Updates | "Noa, what's in the news today?" |

### 🧠 Advanced Memory & Learning (RAG System)
- **Conversation History**: Remembers all interactions with context
- **Personal Preferences**: Learns and adapts to individual user patterns
- **Knowledge Accumulation**: Builds personal knowledge base over time
- **Contextual Responses**: References past conversations naturally
- **Preference Learning**: Adapts responses based on user feedback
- **Multi-session Continuity**: Seamlessly continues conversations across sessions

### 🔧 Modular Hardware Ecosystem

#### Vision Modules 📷
- **Security Camera**: Home monitoring and alerts
- **Person Recognition**: Identifies family members and guests
- **Gesture Control**: Hand gesture recognition for commands
- **Object Detection**: Identifies items and provides information
- **Video Calling**: High-quality video communication

#### Mobility Modules 🛞
- **Autonomous Navigation**: Moves around the house independently
- **Follow Mode**: Tracks and follows specific individuals
- **Patrol Routes**: Programmable movement patterns
- **Obstacle Avoidance**: Smart navigation around furniture and objects
- **Charging Station**: Automatic return to charging dock

#### Sensor Modules 🌡️
- **Environmental**: Temperature, humidity, air quality monitoring
- **Motion Detection**: Presence sensing and activity tracking
- **Sound Detection**: Audio analysis for security and interaction
- **Health Sensors**: Heart rate, stress level monitoring (when applicable)
- **Safety Sensors**: Smoke, gas, water leak detection

## 🚀 Quick Start Guide

### Prerequisites

#### Software Requirements
```bash
# Core Python packages
pip install google-generativeai speech-recognition pyserial
pip install nltk colorama requests beautifulsoup4 markdown
pip install opencv-python numpy pandas

# RAG and Memory System
pip install chromadb sentence-transformers
pip install langchain faiss-cpu

# Smart Home Integration
pip install paho-mqtt requests-oauthlib
pip install home-assistant-api

# Node.js and Electron
npm install electron mongoose noble
```

#### Hardware Requirements

**Basic Setup:**
- Microphone & Speakers for voice interaction
- ESP32 Development Board as main controller
- Bluetooth/WiFi Connection for communication

**Optional Modules:**
- Camera Module (USB webcam or ESP32-CAM)
- Motor Controllers for mobility (L298N, servo motors)
- Sensor Kit (DHT22, PIR, ultrasonic sensors)
- Display Module (OLED or LCD)
- Power Bank for mobile operation

### Installation

1. **Clone the Repository**
```bash
git clone https://github.com/your-username/noa-companion-bot.git
cd noa-companion-bot
```

2. **Install Dependencies**
```bash
# Python dependencies
pip install -r requirements.txt

# Node.js dependencies
npm install
```

3. **Configure API Keys**
```python
# In check2.py, replace with your API keys
genai.configure(api_key="YOUR_GEMINI_API_KEY_HERE")
```

4. **Set Up Piper TTS**
```bash
# Download Piper TTS binary and place in pipers/ folder
# Download voice model (e.g., en_US-hfc_female-medium.onnx)
```

5. **Initialize Memory System**
```bash
python setup_memory_system.py
```

6. **Launch Application**
```bash
npm start
```

## 📱 Operation Modes

### 🏠 Smart Home Mode
```
"Noa, good morning" → Activates morning routine
"Noa, I'm leaving" → Activates away mode with security
"Noa, movie time" → Dims lights, starts entertainment system
```

### 🤖 Companion Mode
```
"Noa, let's chat" → Activates conversational mode with memory context
"Noa, remember this" → Stores important information in long-term memory
"Noa, what did we discuss yesterday?" → Retrieves past conversations
```

### 🔍 Mobile Mode (with wheels)
```
"Noa, follow me" → Activates following behavior
"Noa, patrol the house" → Autonomous security patrol
"Noa, go to kitchen" → Navigation to specific rooms
```

### 📷 Vision Mode (with camera)
```
"Noa, who's at the door?" → Person identification
"Noa, watch the kids" → Monitoring mode with alerts
"Noa, video call grandma" → Initiates video communication
```

## 🎮 Usage Examples

### Memory-Enhanced Conversations
```
User: "Remember, I have a project deadline next Friday"
Noa: *stores in memory* "Got it! I've noted your project deadline for next Friday. Would you like me to set up reminders?"

[Next day]
User: "How's my week looking?"
Noa: *retrieves memory* "You have that important project deadline on Friday that you mentioned yesterday. You also have..."
```

### Smart Home Integration
```
User: "Noa, it's too bright in here"
Noa: *dims lights* "I've dimmed the living room lights. Is this better?"

User: "Noa, play some jazz and set the mood"
Noa: *starts music, adjusts lighting* "Playing jazz playlist and setting ambient lighting. Enjoy!"
```

### Modular Hardware Interaction
```
User: "Noa, show me around the new house"
Noa: *moves with wheels, uses camera* "Let me give you a tour! I can see the living room looks great..."

User: "Noa, check if I left my keys in the bedroom"
Noa: *navigates to bedroom, uses camera* "I can see your keys on the nightstand next to your phone."
```

## 📁 Project Structure

```
noa-advanced-system/
├── core/
│   ├── check2.py              # Main bot logic
│   ├── memory_system.py       # RAG implementation
│   ├── smart_home_controller.py
│   └── module_manager.py
├── modules/
│   ├── camera_module.py
│   ├── mobility_module.py
│   ├── sensor_module.py
│   └── display_module.py
├── interfaces/
│   ├── main.js                # Electron main process
│   ├── dashboard.html         # Control interface
│   ├── user-setup.html        # Profile setup
│   └── profile.html           # Profile management
├── data/
│   ├── memory_db/             # RAG vector database
│   ├── user_profiles/         # User configurations
│   └── module_configs/        # Hardware settings
├── pipers/                    # TTS engine and models
├── package.json               # Node dependencies
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 🔧 Customization & Development

### Adding New Hardware Modules
```python
# Create custom module class
class CustomSensorModule(BaseModule):
    def __init__(self):
        super().__init__("custom_sensor")
    
    def read_data(self):
        # Custom sensor logic
        return sensor_data
    
    def process_command(self, command):
        # Handle voice commands for this module
        pass
```

### Extending Memory System
```python
# Add custom memory categories
memory_system.add_category("project_management")
memory_system.add_category("health_tracking")
memory_system.add_category("learning_progress")
```

## 🔧 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Speech Recognition Not Working | Check microphone permissions, verify internet connection |
| TTS Not Playing | Ensure Piper binary is executable, check audio output device |
| Hardware Not Responding | Check ESP32 connection, verify serial port settings |
| API Errors | Verify Gemini API key, check internet connectivity |
| Memory System Issues | Restart memory database, check vector database integrity |

## 🌟 Why Noa is Revolutionary

### Beyond Traditional Assistants
- **True Memory**: Unlike Alexa/Google that forget conversations, Noa remembers everything
- **Physical Presence**: Mobile robot capabilities with modular hardware
- **Personalized Learning**: Adapts to individual users over time
- **Open Architecture**: Expandable with custom modules and integrations

### Modular Advantage
- **Start Simple**: Begin with basic voice interaction, add modules over time
- **Custom Applications**: Build specialized versions for healthcare, education, security
- **Future-Proof**: Easy to upgrade and expand capabilities
- **Cost-Effective**: Pay only for modules you need

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add some amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Ways to Contribute
- 🔧 **Hardware Modules**: Design new sensors, actuators, and interfaces
- 🧠 **AI Enhancements**: Improve memory systems and conversation quality
- 🏠 **Smart Home Integrations**: Add support for new devices and platforms
- 💻 **User Interfaces**: Create better control and configuration tools

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Google Gemini AI** for conversation intelligence
- **Piper TTS** for high-quality speech synthesis
- **Electron** for cross-platform desktop interface
- **ESP32 Community** for hardware integration examples
- **OpenAI** for inspiration in AI assistant development

## 📞 Support & Community

- **📧 Email**: support@noa-companion.com
- **💬 Discord**: [Join our community](https://discord.gg/noa-companion)
- **📖 Wiki**: [Documentation and tutorials](https://github.com/your-username/noa-companion-bot/wiki)
- **🐛 Issues**: [Report bugs](https://github.com/your-username/noa-companion-bot/issues)

---

<div align="center">

**🚀 Ready to build your own advanced AI companion?**

Start with the basic setup and gradually add modules to create a truly personalized, intelligent assistant that grows with your needs!

**From simple conversations to complex smart home automation, from basic interactions to advanced memory retention - Noa adapts to become exactly what you need.** 🤖✨

[Get Started](https://github.com/your-username/noa-companion-bot/wiki/Quick-Start) | [Documentation](https://github.com/your-username/noa-companion-bot/wiki) | [Community](https://discord.gg/noa-companion)

</div>
