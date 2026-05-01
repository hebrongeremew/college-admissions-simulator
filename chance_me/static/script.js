// Update range value displays
document.getElementById('sat-math').addEventListener('input', function() {
    document.getElementById('sat-math-value').textContent = this.value;
});

document.getElementById('sat-rw').addEventListener('input', function() {
    document.getElementById('sat-rw-value').textContent = this.value;
});

document.getElementById('act').addEventListener('input', function() {
    document.getElementById('act-value').textContent = this.value;
});

document.getElementById('gpa').addEventListener('input', function() {
    document.getElementById('gpa-value').textContent = parseFloat(this.value).toFixed(2);
});

document.getElementById('class-rank').addEventListener('input', function() {
    const rank = parseInt(this.value);
    let rankText = rank + 'th';
    if (rank >= 90) rankText = 'Top 10%';
    else if (rank >= 75) rankText = 'Top 25%';
    else if (rank >= 50) rankText = 'Top 50%';
    document.getElementById('class-rank-value').textContent = rankText;
});

document.getElementById('rigor').addEventListener('input', function() {
    document.getElementById('rigor-value').textContent = this.value + '/10';
});

// Add extracurricular activity
document.getElementById('add-activity').addEventListener('click', function() {
    const container = document.getElementById('activities-container');
    const newActivity = document.createElement('div');
    newActivity.className = 'activity-card';
    newActivity.innerHTML = `
        <select class="activity-category">
            <option value="Leadership">Leadership</option>
            <option value="Academic">Academic</option>
            <option value="Sports">Sports</option>
            <option value="Music">Music</option>
            <option value="Arts">Arts</option>
            <option value="Volunteering">Volunteering</option>
            <option value="Research">Research</option>
            <option value="Clubs">Clubs</option>
        </select>
        <div class="activity-details">
            <input type="number" class="activity-years" placeholder="Years" min="0" max="4" step="1">
            <input type="number" class="activity-hours" placeholder="Hours/week" min="0" max="40" step="1">
        </div>
        <button type="button" class="remove-btn">🗑️</button>
    `;
    container.appendChild(newActivity);
    attachRemoveListener(newActivity.querySelector('.remove-btn'), newActivity);
});

// Add award
document.getElementById('add-award').addEventListener('click', function() {
    const container = document.getElementById('awards-container');
    const newAward = document.createElement('div');
    newAward.className = 'award-card';
    newAward.innerHTML = `
        <select class="award-level">
            <option value="local">🏅 Local</option>
            <option value="regional">🏆 Regional</option>
            <option value="national">🇺🇸 National</option>
            <option value="international">🌍 International</option>
        </select>
        <button type="button" class="remove-btn">🗑️</button>
    `;
    container.appendChild(newAward);
    attachRemoveListener(newAward.querySelector('.remove-btn'), newAward);
});

function attachRemoveListener(btn, element) {
    btn.addEventListener('click', function() {
        element.remove();
    });
}

// Attach remove listeners to existing items
document.querySelectorAll('.activity-card .remove-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        btn.parentElement.remove();
    });
});

document.querySelectorAll('.award-card .remove-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        btn.parentElement.remove();
    });
});

// College selection controls
document.getElementById('select-all').addEventListener('click', function() {
    document.querySelectorAll('.college-checkbox input').forEach(cb => cb.checked = true);
});

document.getElementById('select-none').addEventListener('click', function() {
    document.querySelectorAll('.college-checkbox input').forEach(cb => cb.checked = false);
});

// Form submission
document.getElementById('admission-form').addEventListener('submit', async function(e) {
    e.preventDefault();

    // Show loading state
    const resultsContainer = document.getElementById('results-container');
    const resultsContent = document.getElementById('results-content');
    resultsContainer.style.display = 'block';
    resultsContent.innerHTML = '<div class="loading">📊 Calculating your admission chances...</div>';

    // Collect selected colleges
    const selectedColleges = Array.from(document.querySelectorAll('.college-checkbox input:checked'))
        .map(cb => cb.value);

    if (selectedColleges.length === 0) {
        resultsContent.innerHTML = '<div class="error">⚠️ Please select at least one college to compare.</div>';
        return;
    }

    // Collect extracurriculars
    const extracurriculars = [];
    document.querySelectorAll('#activities-container .activity-card').forEach(card => {
        const category = card.querySelector('.activity-category').value;
        const years = parseInt(card.querySelector('.activity-years')?.value || 0);
        const hours = parseInt(card.querySelector('.activity-hours')?.value || 0);
        extracurriculars.push({ category, years, hours });
    });

    // Collect awards
    const awards = [];
    document.querySelectorAll('#awards-container .award-card').forEach(card => {
        const level = card.querySelector('.award-level').value;
        awards.push({ level });
    });

    // Prepare data payload — all fields the backend expects
    const payload = {
        sat_math: parseInt(document.getElementById('sat-math').value) || 0,
        sat_rw: parseInt(document.getElementById('sat-rw').value) || 0,
        act: parseInt(document.getElementById('act').value) || 0,
        gpa: parseFloat(document.getElementById('gpa').value),
        class_rank: parseInt(document.getElementById('class-rank').value),
        rigor: parseInt(document.getElementById('rigor').value),
        major: document.getElementById('major').value,
        legacy: document.getElementById('legacy').checked,
        first_gen: document.getElementById('first-gen').checked,
        underrepresented: document.getElementById('underrepresented').checked,
        athlete: document.getElementById('athlete').checked,
        faculty_child: document.getElementById('faculty-child').checked,
        extracurriculars,
        awards,
        colleges: selectedColleges
    };

    // Update student badge
    const satMath = payload.sat_math;
    const satRw = payload.sat_rw;
    const act = payload.act;
    let examText = '';
    if (act > 0) {
        examText = `ACT: ${act}`;
    } else if (satMath > 0 || satRw > 0) {
        examText = `SAT: ${satMath + satRw} (M: ${satMath} / RW: ${satRw})`;
    } else {
        examText = 'No test scores entered';
    }
    document.getElementById('student-badge').textContent =
        `${examText} | GPA: ${payload.gpa.toFixed(2)} | Major: ${payload.major}`;

    try {
        const response = await fetch('/evaluate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        if (!response.ok) throw new Error('Network response was not ok');

        const results = await response.json();
        if (results.error) throw new Error(results.error);
        displayResults(results);
    } catch (error) {
        resultsContent.innerHTML = `<div class="error">❌ An error occurred: ${error.message}</div>`;
    }
});

function getCategoryLabel(chance) {
    if (chance >= 60) return { label: 'Safety', cls: 'category-safety' };
    if (chance >= 35) return { label: 'Target', cls: 'category-target' };
    if (chance >= 15) return { label: 'Reach', cls: 'category-reach' };
    return { label: 'Dream', cls: 'category-dream' };
}

function displayResults(results) {
    const resultsContent = document.getElementById('results-content');
    resultsContent.innerHTML = '';

    results.forEach(result => {
        const { label, cls } = getCategoryLabel(result.chance);
        const barWidth = Math.max(result.chance, 5);

        const strengthsHtml = result.strengths.length
            ? result.strengths.map(s => `<li>✅ ${s}</li>`).join('')
            : '<li>None identified</li>';

        const weaknessesHtml = result.weaknesses.length
            ? result.weaknesses.map(w => `<li>⚠️ ${w}</li>`).join('')
            : '<li>None identified</li>';

        const card = document.createElement('div');
        card.className = 'result-card';
        card.innerHTML = `
            <h3>${result.college}</h3>
            <div class="probability-text">${result.chance}%</div>
            <div class="probability-bar">
                <div class="probability-fill" style="width: ${barWidth}%">${result.chance}%</div>
            </div>
            <span class="category-badge ${cls}">${label}</span>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 16px;">
                <div>
                    <strong style="font-size:0.85em; color:#555;">Strengths</strong>
                    <ul style="margin-top:6px; padding-left:16px; font-size:0.85em; color:#333; line-height:1.6;">${strengthsHtml}</ul>
                </div>
                <div>
                    <strong style="font-size:0.85em; color:#555;">Weaknesses</strong>
                    <ul style="margin-top:6px; padding-left:16px; font-size:0.85em; color:#333; line-height:1.6;">${weaknessesHtml}</ul>
                </div>
            </div>
        `;
        resultsContent.appendChild(card);
    });
}