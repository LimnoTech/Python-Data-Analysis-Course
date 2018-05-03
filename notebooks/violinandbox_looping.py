import matplotlib.pyplot as plt
import numpy as np

# Removed random seed

#Make 4 different plots
for i in range(4):
        
    # generate some random test data
    all_data = [np.random.normal(0, std, 100) for std in range(6, 10)]
    
    
    #create figure
    fig = plt.figure(figsize=(11,8))
    #create axes - 1 tall, 2 wide
    
    ax1 = fig.add_subplot(1,2,1)
    # plot violin plot
    ax1.violinplot(all_data,
                   showmeans=False,
                   showmedians=True)
    ax1.set_title('Violin plot')
    ax1.yaxis.grid(True)
    ax1.set_xticks([y + 1 for y in range(len(all_data))])
    ax1.set_xlabel('Four separate samples')
    ax1.set_ylabel('Observed values')
    
    
    ax2 = fig.add_subplot(1,2,2)
    # plot box plot
    ax2.boxplot(all_data)
    ax2.set_title('Box plot')
    ax2.yaxis.grid(True)
    ax2.set_xticks([y + 1 for y in range(len(all_data))])
    ax2.set_xlabel('Four separate samples')
    ax2.set_ylabel('Observed values')
    
    fig.suptitle("Plot number {}".format(i+1))
    
    plt.tight_layout
    plt.savefig("Output_data/violin_box{}.png".format(i+1),dpi=600)
print("hello")