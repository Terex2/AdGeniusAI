import React, { useState } from 'react';
import axios from 'axios';
import { Send, Loader2, Target, PenTool, Image as ImageIcon, Layout, BarChart } from 'lucide-react';

const AdGenerationPage = () => {
  const [formData, setFormData] = useState({
    product_name: '',
    product_description: '',
    price: '',
    target_audience: ''
  });
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await axios.post('http://localhost:8000/api/v1/ads/generate', formData);
      setResult(response.data);
    } catch (error) {
      console.error("Error generating ad:", error);
      alert("حدث خطأ أثناء توليد الإعلان. يرجى المحاولة مرة أخرى.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8 dir-rtl text-right" dir="rtl">
      <div className="max-w-4xl mx-auto">
        <div className="text-center mb-12">
          <h1 className="text-4xl font-extrabold text-gray-900 mb-4">AdGenius AI</h1>
          <p className="text-lg text-gray-600">موظف التسويق الذكي الخاص بك - من الفكرة إلى الحملة</p>
        </div>

        <div className="bg-white shadow-xl rounded-2xl p-8 mb-8">
          <form onSubmit={handleSubmit} className="space-y-6">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">اسم المنتج</label>
                <input
                  type="text"
                  required
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
                  value={formData.product_name}
                  onChange={(e) => setFormData({...formData, product_name: e.target.value})}
                  placeholder="مثال: ساعة ذكية برو"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">السعر</label>
                <input
                  type="text"
                  required
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
                  value={formData.price}
                  onChange={(e) => setFormData({...formData, price: e.target.value})}
                  placeholder="مثال: 299 ريال"
                />
              </div>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">وصف المنتج</label>
              <textarea
                required
                rows="3"
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
                value={formData.product_description}
                onChange={(e) => setFormData({...formData, product_description: e.target.value})}
                placeholder="اشرح مميزات منتجك بالتفصيل..."
              ></textarea>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">الجمهور المستهدف</label>
              <input
                type="text"
                required
                className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
                value={formData.target_audience}
                onChange={(e) => setFormData({...formData, target_audience: e.target.value})}
                placeholder="مثال: الشباب المهتمين بالتقنية والرياضة"
              />
            </div>
            <button
              type="submit"
              disabled={loading}
              className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-lg flex items-center justify-center transition duration-200"
            >
              {loading ? (
                <>
                  <Loader2 className="animate-spin ml-2" />
                  جاري العمل على حملتك...
                </>
              ) : (
                <>
                  <Send className="ml-2" size={20} />
                  ابدأ توليد الحملة
                </>
              )}
            </button>
          </form>
        </div>

        {result && (
          <div className="space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-500">
            {/* Marketing Research */}
            <section className="bg-white shadow rounded-xl p-6">
              <div className="flex items-center mb-4 text-blue-600">
                <Target className="ml-2" />
                <h2 className="text-xl font-bold">تحليل السوق والأبحاث</h2>
              </div>
              <div className="prose max-w-none text-gray-700 whitespace-pre-wrap">
                {result.marketing_plan}
              </div>
            </section>

            {/* Ad Copies */}
            <section className="bg-white shadow rounded-xl p-6">
              <div className="flex items-center mb-4 text-green-600">
                <PenTool className="ml-2" />
                <h2 className="text-xl font-bold">النصوص الإعلانية المقترحة</h2>
              </div>
              <div className="grid gap-6">
                {result.ad_copies.map((copy, index) => (
                  <div key={index} className="p-5 bg-gray-50 rounded-xl border border-gray-200 hover:border-green-300 transition-colors">
                    <h3 className="font-bold text-lg text-green-800 mb-2">{typeof copy === 'object' ? copy.headline : `نسخة ${index + 1}`}</h3>
                    <p className="text-gray-700 mb-4 leading-relaxed">{typeof copy === 'object' ? copy.body : copy}</p>
                    {typeof copy === 'object' && copy.cta && (
                      <div className="inline-block bg-green-600 text-white px-4 py-1 rounded text-sm font-bold">
                        {copy.cta}
                      </div>
                    )}
                  </div>
                ))}
              </div>
            </section>

            {/* Creative Ideas */}
            <section className="bg-white shadow rounded-xl p-6">
              <div className="flex items-center mb-4 text-purple-600">
                <ImageIcon className="ml-2" />
                <h2 className="text-xl font-bold">أفكار التصاميم والبصريات</h2>
              </div>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {result.creative_ideas.map((idea, index) => (
                  <div key={index} className="p-5 bg-purple-50 rounded-xl border border-purple-100 hover:border-purple-300 transition-colors">
                    <h3 className="font-bold text-purple-800 mb-2">{typeof idea === 'object' ? idea.title : `فكرة تصميم ${index + 1}`}</h3>
                    <p className="text-gray-700 leading-relaxed">{typeof idea === 'object' ? idea.description : idea}</p>
                  </div>
                ))}
              </div>
            </section>

            {/* Video Scripts */}
            <section className="bg-white shadow rounded-xl p-6">
              <div className="flex items-center mb-4 text-red-600">
                <Layout className="ml-2" />
                <h2 className="text-xl font-bold">سيناريوهات الفيديو (Reels/TikTok)</h2>
              </div>
              <div className="grid gap-6">
                {result.video_scripts.map((script, index) => (
                  <div key={index} className="p-6 bg-red-50 rounded-xl border border-red-100 hover:border-red-300 transition-colors">
                    <h3 className="font-bold text-lg text-red-800 mb-4">{typeof script === 'object' ? script.title : `سيناريو ${index + 1}`}</h3>
                    {typeof script === 'object' ? (
                      <div className="space-y-3 text-gray-700">
                        <p><span className="font-bold text-red-600">الافتتاحية (Hook):</span> {script.hook}</p>
                        <p><span className="font-bold text-red-600">المحتوى:</span> {script.content}</p>
                        <p><span className="font-bold text-red-600">الخاتمة:</span> {script.cta}</p>
                        <p><span className="font-bold text-red-600 text-sm">الصوت المقترح:</span> <span className="italic">{script.audio}</span></p>
                      </div>
                    ) : (
                      <p className="whitespace-pre-wrap">{script}</p>
                    )}
                  </div>
                ))}
              </div>
            </section>

            {/* Marketing Strategy */}
            <section className="bg-white shadow rounded-xl p-6">
              <div className="flex items-center mb-4 text-orange-600">
                <BarChart className="ml-2" />
                <h2 className="text-xl font-bold">استراتيجية التسويق والخطة</h2>
              </div>
              <div className="prose max-w-none text-gray-700 whitespace-pre-wrap">
                {result.marketing_strategy}
              </div>
            </section>
          </div>
        )}
      </div>
    </div>
  );
};

export default AdGenerationPage;
