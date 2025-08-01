import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.patches import Circle
import os

def create_video_animation():
    """Create and save the toy journey animation as a video file"""
    
    # Set up the figure
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    
    # Supply chain stages
    stages = [
        {"name": "Oil (Saudi Arabia)", "pos": (1, 6), "cost": 0.45, "emotion": "😰", "color": "black"},
        {"name": "Refining (Singapore)", "pos": (2.5, 6), "cost": 0.53, "emotion": "✨", "color": "gray"},
        {"name": "Ethylene (China)", "pos": (4, 6), "cost": 0.08, "emotion": "🤔", "color": "lightblue"},
        {"name": "PVC Creation", "pos": (5.5, 6), "cost": 0.55, "emotion": "😕", "color": "white"},
        {"name": "Mold Injection", "pos": (7, 6), "cost": 1.93, "emotion": "😣", "color": "pink"},
        {"name": "Painting", "pos": (8.5, 6), "cost": 0.08, "emotion": "🎨", "color": "yellow"},
        {"name": "Assembly", "pos": (2, 4), "cost": 0.55, "emotion": "😊", "color": "green"},
        {"name": "Quality Check", "pos": (4, 4), "cost": 0.08, "emotion": "😰", "color": "orange"},
        {"name": "Packaging", "pos": (6, 4), "cost": 0.08, "emotion": "🤷‍♂️", "color": "purple"},
        {"name": "Shipping", "pos": (8, 4), "cost": 0.53, "emotion": "🌍", "color": "blue"},
        {"name": "Store Shelf", "pos": (5, 2), "cost": 0.08, "emotion": "👀", "color": "red"},
        {"name": "Price Discovery", "pos": (5, 0.5), "cost": 745, "emotion": "😱", "color": "darkred"}
    ]
    
    def animate(frame):
        ax.clear()
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.set_aspect('equal')
        
        # Draw supply chain stages
        for i, stage in enumerate(stages):
            circle = Circle(stage["pos"], 0.3, color=stage["color"], alpha=0.7)
            ax.add_patch(circle)
            
            ax.text(stage["pos"][0], stage["pos"][1] + 0.5, stage["name"], 
                   ha='center', va='bottom', fontsize=8, fontweight='bold')
            
            ax.text(stage["pos"][0], stage["pos"][1] - 0.5, f"${stage['cost']:.2f}", 
                   ha='center', va='top', fontsize=7)
            
            ax.text(stage["pos"][0], stage["pos"][1], stage["emotion"], 
                   ha='center', va='center', fontsize=16)
        
        # Animate toy movement
        if frame < 120:
            progress = frame / 120
            stage_idx = int(progress * (len(stages) - 1))
            
            if stage_idx < len(stages) - 1:
                start_pos = stages[stage_idx]["pos"]
                end_pos = stages[stage_idx + 1]["pos"]
                
                toy_x = start_pos[0] + (end_pos[0] - start_pos[0]) * (progress * (len(stages) - 1) - stage_idx)
                toy_y = start_pos[1] + (end_pos[1] - start_pos[1]) * (progress * (len(stages) - 1) - stage_idx)
                
                toy_emotion = stages[stage_idx]["emotion"]
                toy_color = stages[stage_idx]["color"]
                total_cost = sum(stages[i]["cost"] for i in range(stage_idx + 1))
                
                journey_text = f"Stage {stage_idx + 1}: {stages[stage_idx]['name']}\nCost so far: ${total_cost:.2f}"
                
            else:
                toy_x, toy_y = stages[-1]["pos"]
                toy_emotion = "😱"
                toy_color = "darkred"
                total_cost = 745
                journey_text = "PRICE DISCOVERY!\nMaterial cost: $8.84\nStore price: $745\nMARKUP: 84x!"
        else:
            toy_x, toy_y = stages[-1]["pos"]
            toy_emotion = "😱"
            toy_color = "darkred"
            journey_text = "THE SHOCKING TRUTH!"
        
        # Draw the toy
        toy_circle = Circle((toy_x, toy_y), 0.4, color=toy_color, alpha=0.9, edgecolor='black', linewidth=2)
        ax.add_patch(toy_circle)
        ax.text(toy_x, toy_y, toy_emotion, ha='center', va='center', fontsize=20)
        
        # Add journey text
        ax.text(0.5, 7.5, journey_text, fontsize=12, fontweight='bold', 
               bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.8))
        
        # Add title
        if frame < 120:
            ax.text(5, 7.8, "🧸 TOY'S EMOTIONAL JOURNEY THROUGH THE SUPPLY CHAIN 🧸", 
                   ha='center', fontsize=14, fontweight='bold')
        else:
            ax.text(5, 7.8, "🚨 THE SHOCKING TRUTH REVEALED! 🚨", 
                   ha='center', fontsize=14, fontweight='bold', color='red')
        
        # Add final reveal
        if frame >= 120:
            ax.text(0.5, 1.5, f"Material Cost: ${8.84:.2f}\nCollector Price: ${745}\nMARKUP: 84x!", 
                   fontsize=12, fontweight='bold', color='red',
                   bbox=dict(boxstyle='round,pad=0.5', facecolor='lightcoral', alpha=0.9))
    
    # Create animation
    anim = animation.FuncAnimation(fig, animate, frames=150, interval=100, repeat=False)
    
    # Save as MP4
    print("🎬 Saving animation as MP4...")
    try:
        anim.save('toy_journey_animation.mp4', writer='ffmpeg', fps=10, dpi=100)
        print("✅ Animation saved as 'toy_journey_animation.mp4'")
    except Exception as e:
        print(f"❌ Error saving MP4: {e}")
        print("💡 Try installing ffmpeg: brew install ffmpeg")
    
    # Save as GIF
    print("🎬 Saving animation as GIF...")
    try:
        anim.save('toy_journey_animation.gif', writer='pillow', fps=10)
        print("✅ Animation saved as 'toy_journey_animation.gif'")
    except Exception as e:
        print(f"❌ Error saving GIF: {e}")
    
    plt.close()
    return anim

def main():
    """Main function"""
    print("🎬 TOY JOURNEY ANIMATION VIDEO CREATOR")
    print("=" * 50)
    
    anim = create_video_animation()
    
    print("\n📁 Files created:")
    print("- toy_journey_animation.mp4 (if ffmpeg is installed)")
    print("- toy_journey_animation.gif")
    print("\n🌐 To use on your website:")
    print("1. Upload the video files to your web server")
    print("2. Use HTML5 <video> tag or <img> tag for GIF")
    print("3. Or embed the interactive HTML version (toy_journey_web.html)")

if __name__ == "__main__":
    main() 