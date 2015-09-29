Name     : rubygem-gritter
Version  : 1.1.0
Release  : 4
URL      : https://rubygems.org/downloads/gritter-1.1.0.gem
Source0  : https://rubygems.org/downloads/gritter-1.1.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-rdoc

%description
# gritter
version 1.1.0
Robin Brouwer
montblanc
This Ruby on Rails gem allows you to easily add Growl-like notifications to your application using a jQuery plugin called 'gritter'. [Check out the demo for this plugin](http://boedesign.com/demos/gritter/).

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n gritter-1.1.0
gem spec %{SOURCE0} -l --ruby > rubygem-gritter.gemspec

%build
gem build rubygem-gritter.gemspec

%install
gem_dir=$(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--install-dir .${gem_dir} \
--bindir .%{_bindir} \
gritter-1.1.0.gem

mkdir -p %{buildroot}${gem_dir}
cp -pa .${gem_dir}/* \
%{buildroot}${gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/gritter-1.1.0.gem
/usr/lib64/ruby/gems/2.2.0/doc/gritter-1.1.0/ri/Gritter/Engine/cdesc-Engine.ri
/usr/lib64/ruby/gems/2.2.0/doc/gritter-1.1.0/ri/Gritter/Gflash/cdesc-Gflash.ri
/usr/lib64/ruby/gems/2.2.0/doc/gritter-1.1.0/ri/Gritter/Gflash/gflash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gritter-1.1.0/ri/Gritter/Gflash/gflash_push-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gritter-1.1.0/ri/Gritter/Gflash/gflash_text-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gritter-1.1.0/ri/Gritter/Gflash/gflash_translation-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gritter-1.1.0/ri/Gritter/Gflash/redirect_to-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gritter-1.1.0/ri/Gritter/Helpers/add_gritter-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gritter-1.1.0/ri/Gritter/Helpers/cdesc-Helpers.ri
/usr/lib64/ruby/gems/2.2.0/doc/gritter-1.1.0/ri/Gritter/Helpers/extend_gritter-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gritter-1.1.0/ri/Gritter/Helpers/get_translation-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gritter-1.1.0/ri/Gritter/Helpers/gflash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gritter-1.1.0/ri/Gritter/Helpers/gflash_titles-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gritter-1.1.0/ri/Gritter/Helpers/js-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gritter-1.1.0/ri/Gritter/Helpers/remove_gritter-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gritter-1.1.0/ri/Gritter/LocaleGenerator/cdesc-LocaleGenerator.ri
/usr/lib64/ruby/gems/2.2.0/doc/gritter-1.1.0/ri/Gritter/LocaleGenerator/copy_gflash_locale-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/gritter-1.1.0/ri/Gritter/Railtie/cdesc-Railtie.ri
/usr/lib64/ruby/gems/2.2.0/doc/gritter-1.1.0/ri/Gritter/cdesc-Gritter.ri
/usr/lib64/ruby/gems/2.2.0/doc/gritter-1.1.0/ri/Gritter/initialize-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/gritter-1.1.0/ri/Gritter/rails_flash_fallback%3d-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/gritter-1.1.0/ri/Gritter/rails_flash_fallback-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/gritter-1.1.0/ri/Rails/cdesc-Rails.ri
/usr/lib64/ruby/gems/2.2.0/doc/gritter-1.1.0/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/gritter-1.1.0/ri/lib/generators/gritter/page-USAGE.ri
/usr/lib64/ruby/gems/2.2.0/gems/gritter-1.1.0/.gitignore
/usr/lib64/ruby/gems/2.2.0/gems/gritter-1.1.0/Gemfile
/usr/lib64/ruby/gems/2.2.0/gems/gritter-1.1.0/README.md
/usr/lib64/ruby/gems/2.2.0/gems/gritter-1.1.0/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/gritter-1.1.0/gritter.gemspec
/usr/lib64/ruby/gems/2.2.0/gems/gritter-1.1.0/init.rb
/usr/lib64/ruby/gems/2.2.0/gems/gritter-1.1.0/lib/generators/gritter/USAGE
/usr/lib64/ruby/gems/2.2.0/gems/gritter-1.1.0/lib/generators/gritter/locale_generator.rb
/usr/lib64/ruby/gems/2.2.0/gems/gritter-1.1.0/lib/generators/gritter/templates/gflash.en.yml
/usr/lib64/ruby/gems/2.2.0/gems/gritter-1.1.0/lib/gritter.rb
/usr/lib64/ruby/gems/2.2.0/gems/gritter-1.1.0/lib/gritter/engine.rb
/usr/lib64/ruby/gems/2.2.0/gems/gritter-1.1.0/lib/gritter/gflash.rb
/usr/lib64/ruby/gems/2.2.0/gems/gritter-1.1.0/lib/gritter/helpers.rb
/usr/lib64/ruby/gems/2.2.0/gems/gritter-1.1.0/lib/gritter/railtie.rb
/usr/lib64/ruby/gems/2.2.0/gems/gritter-1.1.0/lib/gritter/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/gritter-1.1.0/vendor/assets/images/error.png
/usr/lib64/ruby/gems/2.2.0/gems/gritter-1.1.0/vendor/assets/images/gritter-close.png
/usr/lib64/ruby/gems/2.2.0/gems/gritter-1.1.0/vendor/assets/images/gritter.png
/usr/lib64/ruby/gems/2.2.0/gems/gritter-1.1.0/vendor/assets/images/ie-spacer.gif
/usr/lib64/ruby/gems/2.2.0/gems/gritter-1.1.0/vendor/assets/images/notice.png
/usr/lib64/ruby/gems/2.2.0/gems/gritter-1.1.0/vendor/assets/images/progress.gif
/usr/lib64/ruby/gems/2.2.0/gems/gritter-1.1.0/vendor/assets/images/success.png
/usr/lib64/ruby/gems/2.2.0/gems/gritter-1.1.0/vendor/assets/images/warning.png
/usr/lib64/ruby/gems/2.2.0/gems/gritter-1.1.0/vendor/assets/javascripts/gritter.js
/usr/lib64/ruby/gems/2.2.0/gems/gritter-1.1.0/vendor/assets/stylesheets/gritter.css.scss
/usr/lib64/ruby/gems/2.2.0/specifications/gritter-1.1.0.gemspec
