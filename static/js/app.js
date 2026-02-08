/**
 * Placement Predictor - Frontend JavaScript
 */

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('prediction-form');
    const submitBtn = document.getElementById('submit-btn');
    const btnText = submitBtn.querySelector('.btn-text');
    const btnIcon = submitBtn.querySelector('.btn-icon');
    const btnLoader = submitBtn.querySelector('.btn-loader');
    const resultsCard = document.getElementById('results-card');
    const resetBtn = document.getElementById('reset-btn');

    // Form submission handler
    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Show loading state
        setLoading(true);

        // Collect form data
        const formData = {
            iq: document.getElementById('iq').value,
            cgpa: document.getElementById('cgpa').value,
            prev_sem_result: document.getElementById('prev_sem_result').value,
            academic_performance: document.getElementById('academic_performance').value,
            internship_experience: document.getElementById('internship_experience').value,
            extra_curricular_score: document.getElementById('extra_curricular_score').value,
            communication_skills: document.getElementById('communication_skills').value,
            projects_completed: document.getElementById('projects_completed').value
        };

        try {
            const response = await fetch('/api/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });

            const data = await response.json();

            if (response.ok) {
                displayResults(data);
            } else {
                showError(data.error || 'Prediction failed. Please try again.');
            }
        } catch (error) {
            console.error('Error:', error);
            showError('Network error. Please check your connection.');
        } finally {
            setLoading(false);
        }
    });

    // Reset button handler
    resetBtn.addEventListener('click', () => {
        resultsCard.classList.add('hidden');
        form.reset();
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    /**
     * Toggle loading state
     */
    function setLoading(isLoading) {
        submitBtn.disabled = isLoading;

        if (isLoading) {
            btnText.style.opacity = '0';
            btnIcon.style.opacity = '0';
            btnLoader.classList.remove('hidden');
        } else {
            btnText.style.opacity = '1';
            btnIcon.style.opacity = '1';
            btnLoader.classList.add('hidden');
        }
    }

    /**
     * Display prediction results
     */
    function displayResults(data) {
        const placementStatus = document.getElementById('placement-status');
        const placementIcon = document.getElementById('placement-icon');
        const salaryValue = document.getElementById('salary-value');
        const salaryResult = document.getElementById('salary-result');

        // Update placement status
        if (data.placed) {
            placementStatus.textContent = 'Likely to be Placed! 🎉';
            placementStatus.className = 'result-value success';
            placementIcon.textContent = '✅';
        } else {
            placementStatus.textContent = 'Needs Improvement';
            placementStatus.className = 'result-value warning';
            placementIcon.textContent = '📚';
        }

        // Update salary
        if (data.placed && data.salary > 0) {
            salaryResult.style.display = 'flex';
            salaryValue.textContent = formatSalary(data.salary);
            salaryValue.className = 'result-value success';
        } else {
            salaryResult.style.display = 'none';
        }

        // Show results card with animation
        resultsCard.classList.remove('hidden');

        // Scroll to results
        setTimeout(() => {
            resultsCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }, 100);
    }

    /**
     * Format salary for display
     */
    function formatSalary(salary) {
        if (salary >= 100000) {
            return '₹' + (salary / 100000).toFixed(2) + ' LPA';
        } else if (salary >= 1000) {
            return '₹' + (salary / 1000).toFixed(1) + 'K';
        }
        return '₹' + salary.toFixed(0);
    }

    /**
     * Show error message
     */
    function showError(message) {
        const placementStatus = document.getElementById('placement-status');
        const placementIcon = document.getElementById('placement-icon');
        const salaryResult = document.getElementById('salary-result');

        placementStatus.textContent = message;
        placementStatus.className = 'result-value';
        placementStatus.style.color = '#ef4444';
        placementIcon.textContent = '❌';
        salaryResult.style.display = 'none';

        resultsCard.classList.remove('hidden');
        resultsCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }

    // Add input animations
    const inputs = document.querySelectorAll('input, select');
    inputs.forEach(input => {
        input.addEventListener('focus', () => {
            input.parentElement.style.transform = 'scale(1.02)';
        });

        input.addEventListener('blur', () => {
            input.parentElement.style.transform = 'scale(1)';
        });
    });
});
