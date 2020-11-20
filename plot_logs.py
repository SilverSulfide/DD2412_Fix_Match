from tensorboard.backend.event_processing.event_accumulator import EventAccumulator
event_acc = EventAccumulator('results/saved_models_0_base/cifar10_40/tensorboard')
event_acc.Reload()
# Show all tags in the log file
print(event_acc.Tags())
print("Done")
# E. g. get wall clock, number of steps and value for a scalar 'Accuracy'
#sup_loss, unsup_loss, total_loss, lr, mask, time, run_time, ev_loss, acc = zip(*event_acc.Scalars)
z = event_acc.Scalars('train/total_loss')
loss = [i.value for i in z]
x = list(range(len(loss)))
import matplotlib.pyplot as plt
plt.plot(x, loss)
plt.show()