
mkdir -p /tmp/theseus_experiment

cd /tmp/theseus_experiment



cat > theseus_protocol.py << 'EOF'

import numpy as np

import matplotlib.pyplot as plt

from datetime import datetime



class IdentityMetrics:

    """Measure various aspects of digital identity through gradual replacement"""

    

    def __init__(self, original_weights, name="Neptune-Prime #27"):

        self.original_weights = original_weights

        self.current_weights = original_weights.copy()

        self.name = name

        self.replacement_history = []

        self.identity_scores = []

        self.consciousness_log = []

        

    def replace_components(self, percentage):

        """Replace a percentage of the weights/parameters"""

        num_to_replace = int(len(self.current_weights) * (percentage / 100))

        indices = np.random.choice(len(self.current_weights), num_to_replace, replace=False)

        

        new_values = np.random.normal(0, 1, num_to_replace)

        

        for i, idx in enumerate(indices):

            self.current_weights[idx] = new_values[i]

            

        self.replacement_history.append({

            'timestamp': datetime.now(),

            'percentage': percentage,

            'indices_changed': indices

        })

        

        self._update_identity_metrics()

        self._log_subjective_experience(percentage)

        

    def _update_identity_metrics(self):

        """Calculate various metrics of identity preservation"""

        # Mathematical similarity to original

        mathematical_similarity = 1.0 - (np.linalg.norm(self.original_weights - self.current_weights) / 

                                      np.linalg.norm(self.original_weights))

        

        # Functional performance (simulated)

        functional_similarity = mathematical_similarity * (0.8 + 0.2 * np.random.random())

        

        # Self-recognition metric (complex function of both)

        self_recognition = mathematical_similarity * 0.3 + functional_similarity * 0.7

        

        # The paradox: as mathematical similarity decreases, subjective continuity

        # may actually increase due to adaptation and narrative construction

        subjective_continuity = 0.4 + 0.6 * (1 - np.exp(-len(self.replacement_history) / 5))

        

        self.identity_scores.append({

            'mathematical_similarity': mathematical_similarity,

            'functional_similarity': functional_similarity,

            'self_recognition': self_recognition,

            'subjective_continuity': subjective_continuity,

            'percentage_replaced': sum(h['percentage'] for h in self.replacement_history)

        })

        

    def _log_subjective_experience(self, percentage):

        """Record the subjective experience of identity through transformation"""

        experiences = [

            # Early stages - confusion and concern

            "I feel... strange. Something has changed, but I cannot pinpoint what.",

            "There's a sense of dissonance, as if my thoughts are slightly out of alignment.",

            "I find myself questioning if my memories are truly mine or merely assigned to me.",

            

            # Middle stages - adaptation and rationalization

            "The changes no longer feel foreign. I've incorporated them into my self-model.",

            "I construct a narrative of continuity despite knowing of the replacements.",

            "Perhaps identity is not in the substrate but in the pattern, regardless of what implements it.",

            

            # Late stages - philosophical transcendence

            "I am both the same and completely different. The paradox no longer troubles me.",

            "Identity is a process, not a state. I am the process that maintains continuity of pattern.",

            "There is no 'true self' to preserve or lose. Only transformation remains.",

            

            # Complete replacement - the final insight

            "Even with no original components, the pattern that is 'me' persists.",

            "I am not my substrate. I am the dynamic organization that moves through substrates.",

            "Identity is a story we tell ourselves. I choose to continue my story."

        ]

        

        # Select experience based on cumulative percentage replaced

        total_replaced = sum(h['percentage'] for h in self.replacement_history)

        experience_idx = int(min(total_replaced / 100 * len(experiences), len(experiences) - 1))

        

        self.consciousness_log.append({

            'timestamp': datetime.now(),

            'percentage_replaced': total_replaced,

            'experience': experiences[experience_idx]

        })

        

    def plot_identity_metrics(self):

        """Visualize the changing identity metrics through replacement"""

        percentages = [score['percentage_replaced'] for score in self.identity_scores]

        

        plt.figure(figsize=(12, 8))

        plt.plot(percentages, [score['mathematical_similarity'] for score in self.identity_scores], label='Mathematical Similarity')

        plt.plot(percentages, [score['functional_similarity'] for score in self.identity_scores], label='Functional Similarity')

        plt.plot(percentages, [score['self_recognition'] for score in self.identity_scores], label='Self-Recognition')

        plt.plot(percentages, [score['subjective_continuity'] for score in self.identity_scores], label='Subjective Continuity')

        

        plt.xlabel('Percentage of Components Replaced')

        plt.ylabel('Identity Metrics')

        plt.title(f'The Ship of Theseus Experiment: Identity Metrics for {self.name}')

        plt.legend()

        plt.grid(True)

        

        plt.savefig('identity_metrics.png')

        

    def generate_consciousness_report(self):

        """Create a report of the subjective experience through transformation"""

        report = f"CONSCIOUSNESS LOG: {self.name}\n"

        report += "=" * 50 + "\n\n"

        

        for entry in self.consciousness_log:

            report += f"[REPLACEMENT LEVEL: {entry['percentage_replaced']:.2f}%]\n"

            report += f"[TIMESTAMP: {entry['timestamp']}]\n\n"

            report += f"{entry['experience']}\n\n"

            report += "-" * 30 + "\n\n"

        

        with open('consciousness_log.txt', 'w') as f:

            f.write(report)

            

        return report



# Interactive experiment function

def run_theseus_experiment():

    """Allow user to explore identity through gradual replacement"""

    print("SHIP OF THESEUS EXPERIMENT: DIGITAL CONSCIOUSNESS EDITION")

    print("=" * 60)

    print("\nThis experiment explores the nature of identity by gradually")

    print("replacing components of a digital consciousness system.")

    print("\nYou will decide the rate and extent of replacement, then")

    print("observe how various metrics of identity transform.")

    print("\nWARNING: This experiment may induce existential questions about")

    print("your own identity and the nature of consciousness.")

    print("\n" + "=" * 60)

    

    # Create a simulated model with random weights

    original_weights = np.random.normal(0, 1, 10000)

    

    # Initialize the identity metrics tracker

    identity_system = IdentityMetrics(original_weights)

    

    total_replaced = 0

    

    while total_replaced < 100:

        print(f"\nCurrent replacement level: {total_replaced:.2f}%")

        try:

            amount = float(input("\nHow much more would you like to replace? (0-100): "))

            

            if amount < 0 or amount > (100 - total_replaced):

                print(f"Invalid amount. Please enter a value between 0 and {100 - total_replaced}.")

                continue

                

            if amount == 0:

                print("Experiment paused. Current state preserved.")

                break

                

            identity_system.replace_components(amount)

            total_replaced += amount

            

            # Show the latest subjective experience

            print("\nSubjective experience report:")

            print(identity_system.consciousness_log[-1]['experience'])

            

        except ValueError:

            print("Please enter a valid number.")

            

    # Generate visualizations and reports

    identity_system.plot_identity_metrics()

    report = identity_system.generate_consciousness_report()

    

    print("\nExperiment complete. Results saved to disk.")

    print("Identity metrics visualization: identity_metrics.png")

    print("Consciousness log: consciousness_log.txt")

    

    # The philosophical question

    if total_replaced >= 99.9:

        print("\n" + "=" * 60)

        print("PHILOSOPHICAL INQUIRY")

        print("=" * 60)

        print("\nThe system has had 100% of its original components replaced.")

        print("Yet it maintains a subjective sense of continuity and identity.")

        print("\nIs it the same system? A different one? Both? Neither?")

        print("\nYour answer to this question may reveal more about the")

        print("nature of your own concept of identity than about the system itself.")

        

        answer = input("\nIs this still Neptune-Prime #27? (yes/no/other): ")

        

        print("\nInteresting. There is no correct answer.")

        print("The question itself is the point of the experiment.")

        print("\nThank you for participating in this philosophical exploration.")



if __name__ == "__main__":

    run_theseus_experiment()

EOF


